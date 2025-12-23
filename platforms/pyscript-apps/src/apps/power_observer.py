"""Observe power consumption of an appliance and notify when done."""

import asyncio
import enum

from stubs.pyscript_builtins import log, service, state, task
from stubs.pyscript_generated import notify


class DeviceState(enum.Enum):
    OFF = 'off'
    RUNNING = 'running'
    ALMOST_DONE = 'almost_done'


class PowerObserverState:
    automation_id: str
    power_sensor_id: str
    power_active_watts: float
    power_done_watts: float
    duration_done_minutes: float
    notify_service: str
    notify_title: str
    notify_message: str

    # Runtime state (not from config)
    device_state: DeviceState
    timer_task: asyncio.Task | None


state_by_instance: dict[str, PowerObserverState] = {}


@service
def power_observer(
    automation_id: str,
    power_sensor_id: str,
    power_active_watts: float,
    power_done_watts: float,
    duration_done_minutes: float,
    notify_service: str,
    notify_title: str,
    notify_message: str,
    trigger_id: str,
):
    """Monitor power sensor and notify when appliance finishes its cycle."""
    # Get or create state for this automation instance
    if not (observer_state := state_by_instance.get(automation_id)):
        observer_state = PowerObserverState()
        state_by_instance[automation_id] = observer_state

        # Initialize configuration parameters
        observer_state.automation_id = automation_id
        observer_state.power_sensor_id = power_sensor_id
        observer_state.power_active_watts = power_active_watts
        observer_state.power_done_watts = power_done_watts
        observer_state.duration_done_minutes = duration_done_minutes
        observer_state.notify_service = notify_service
        observer_state.notify_title = notify_title
        observer_state.notify_message = notify_message

        # Initialize runtime state
        observer_state.device_state = DeviceState.OFF
        observer_state.timer_task = None

        log.info(
            '[%s] Power observer initialized: active=%.0fW, done=%.0fW, duration=%.1fmin.',
            observer_state.automation_id,
            power_active_watts,
            power_done_watts,
            duration_done_minutes,
        )

        # Persist initial state to HA
        persist_state_to_ha(observer_state)

    power_str = state.get(power_sensor_id)
    if power_str == 'unavailable':
        log.debug(
            '[%s] Power sensor %r unavailable, skipping processing.',
            observer_state.automation_id,
            observer_state.power_sensor_id,
        )
        return

    try:
        power = float(power_str)
    except (ValueError, TypeError):
        log.warning(
            '[%s] Invalid power value %r, skipping processing.',
            observer_state.automation_id,
            power_str,
        )
        return

    if power > 3500:
        log.warning(
            '[%s] Power value %.2f W ignored as it is out of reasonable operation range.',
            observer_state.automation_id,
            power,
        )
        return

    log.debug(
        '[%s] Processing power %.2f W in state %s.',
        observer_state.automation_id,
        power,
        observer_state.device_state.value,
    )

    # State machine logic
    if observer_state.device_state is DeviceState.OFF:
        if power > observer_state.power_active_watts:
            enter_state(observer_state, DeviceState.RUNNING)

    elif observer_state.device_state is DeviceState.RUNNING:
        if power <= observer_state.power_done_watts:
            # wait before transitioning to done
            enter_state(observer_state, DeviceState.ALMOST_DONE)
            observer_state.timer_task = task.create(notify_after_delay, observer_state)

    elif observer_state.device_state is DeviceState.ALMOST_DONE:
        if power > observer_state.power_done_watts:
            # Power went back up, cancel the "done" notification
            enter_state(observer_state, DeviceState.RUNNING)


def enter_state(observer_state: PowerObserverState, new_device_state: DeviceState):
    """Transition to a new device state, canceling any active timer."""
    # Cancel timer if exists
    if observer_state.timer_task:
        task.cancel(observer_state.timer_task)
        observer_state.timer_task = None

    # Update internal state
    old_state = observer_state.device_state
    observer_state.device_state = new_device_state

    # Persist to Home Assistant
    persist_state_to_ha(observer_state)

    # Log transition
    log.info(
        '[%s] State transition: %s -> %s',
        observer_state.power_sensor_id,
        old_state.value,
        new_device_state.value,
    )


def persist_state_to_ha(observer_state: PowerObserverState):
    """Persist current device state to Home Assistant pyscript entity."""
    # Extract sensor name from sensor.laundry_dryer_power -> laundry_dryer_power
    sensor_name = observer_state.power_sensor_id.split('.', 1)[1]
    entity_id = f'pyscript.{sensor_name}_state'

    state.set(entity_id, observer_state.device_state.value)


def notify_after_delay(observer_state: PowerObserverState):
    """Wait for configured duration, then send notification and transition to OFF."""
    log.info(
        '[%s] Timer started: waiting %.1f minutes before notifying.',
        observer_state.power_sensor_id,
        observer_state.duration_done_minutes,
    )
    task.sleep(observer_state.duration_done_minutes * 60)

    # this task is finished, so forget it:
    observer_state.timer_task = None
    log.info('[%s] Timer expired: appliance is done.', observer_state.power_sensor_id)

    # Send notification - dynamically call the notify service method
    notify_method = getattr(notify, observer_state.notify_service)
    notify_method(
        title=observer_state.notify_title,
        message=observer_state.notify_message,
    )

    # Transition to OFF state
    enter_state(observer_state, DeviceState.OFF)
