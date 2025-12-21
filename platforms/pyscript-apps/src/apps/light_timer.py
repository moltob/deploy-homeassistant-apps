import asyncio

from stubs.pyscript_builtins import log, service, task
from stubs.pyscript_generated import light


class TimerState:
    automation_id: str
    entity_id: str
    duration: int
    task: asyncio.Task | None


state_by_instance: dict[str, TimerState] = {}


@service
def light_timer(automation_id: str, entity_id: str, duration: int, new_state: str):
    # Get or create state for this automation instance with configuration parameters
    if not (state := state_by_instance.get(automation_id)):
        state = TimerState()
        state_by_instance[automation_id] = state

        state.automation_id = automation_id
        state.entity_id = entity_id
        state.duration = duration
        state.task = None

        log.info('[%s] Initializing.', state.automation_id)

    # Cancel existing timer task if any
    if state.task:
        log.info('[%s] Cancelling timer to turn off.', state.automation_id)
        task.cancel(state.task)
        state.task = None

    # Process trigger parameter (new_state)
    if new_state == 'on':
        state.task = task.create(turn_off_light_after, state)


def turn_off_light_after(state: TimerState):
    log.info('[%s] Scheduling to turn off after %d minutes.', state.automation_id, state.duration)
    task.sleep(state.duration * 60)
    log.info('[%s] Timer expired, turning off.', state.automation_id)
    light.turn_off(entity_id=state.entity_id)
    state.task = None
