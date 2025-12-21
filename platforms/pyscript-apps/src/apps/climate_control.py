"""Climate control for radiators based on external temperature sensor and schedules."""

import datetime

from stubs.pyscript_builtins import log, service, state
from stubs.pyscript_generated import climate


class ClimateState:
    automation_id: str
    radiator_id: str
    temperature_sensor_id: str
    window_ids: list[str]
    comfort_temp_id: str
    eco_temp_id: str
    comfort_start_id: str
    comfort_stop_id: str


state_by_instance: dict[str, ClimateState] = {}


@service
def climate_control(
    automation_id: str,
    radiator_id: str,
    temperature_sensor_id: str,
    window_ids: list[str],
    comfort_temp_id: str,
    eco_temp_id: str,
    comfort_start_id: str,
    comfort_stop_id: str,
    trigger_id: str,
):
    # Get or create state for this automation instance
    if not (climate_state := state_by_instance.get(automation_id)):
        climate_state = ClimateState()
        state_by_instance[automation_id] = climate_state

        climate_state.automation_id = automation_id
        climate_state.radiator_id = radiator_id
        climate_state.temperature_sensor_id = temperature_sensor_id
        climate_state.window_ids = window_ids
        climate_state.comfort_temp_id = comfort_temp_id
        climate_state.eco_temp_id = eco_temp_id
        climate_state.comfort_start_id = comfort_start_id
        climate_state.comfort_stop_id = comfort_stop_id

        log.info(
            '[%s] Climate control initialized with sensor=%r, %d windows.',
            climate_state.automation_id,
            temperature_sensor_id,
            len(window_ids),
        )

    log.info(
        '[%s] Processing trigger %r for automation %r.',
        climate_state.automation_id,
        trigger_id,
        automation_id,
    )
    control_radiator(climate_state)


def control_radiator(climate_state: ClimateState):
    """Main control logic for radiator based on windows, time schedule, and temperature."""
    # Stop heating if any window is open
    for window_id in climate_state.window_ids:
        if state.get(window_id) == 'on':
            set_temperature(climate_state, 0.0, 'Window open')
            return

    # Check time if in eco or comfort mode
    now = datetime.datetime.now().time()
    comfort_start = datetime.time.fromisoformat(state.get(climate_state.comfort_start_id))
    comfort_stop = datetime.time.fromisoformat(state.get(climate_state.comfort_stop_id))

    if comfort_start <= now < comfort_stop:
        target_temp = float(state.get(climate_state.comfort_temp_id))
        set_temperature(climate_state, target_temp, 'Comfort mode')
    else:
        target_temp = float(state.get(climate_state.eco_temp_id))
        set_temperature(climate_state, target_temp, 'Eco mode')


def set_temperature(climate_state: ClimateState, target_temperature: float, reason: str):
    """Set radiator temperature with offset compensation based on actual vs apparent temperature."""
    radiator_attrs = state.getattr(climate_state.radiator_id)
    assert radiator_attrs, 'radiator has attributes'

    apparent_temperature = float(radiator_attrs.get('current_temperature', 0))
    actual_temperature = float(state.get(climate_state.temperature_sensor_id))

    # Get radiator temperature limits
    max_temperature = int(radiator_attrs.get('max_temp', 30))

    if target_temperature > 0 and actual_temperature < target_temperature:
        # Calculate offset: if radiator sensor reads higher than actual, we need to compensate
        offset = max(0.0, 2 * (apparent_temperature - actual_temperature))
        set_temperature = min(max_temperature, int(round(target_temperature + offset, 0)))
        set_mode = 'heat'

        log.info(
            '[%s] %s: target = %s, apparent = %s, actual = %s, set = %s, mode=%r.',
            climate_state.automation_id,
            reason,
            target_temperature,
            apparent_temperature,
            actual_temperature,
            set_temperature,
            set_mode,
        )

        climate.set_temperature(
            entity_id=climate_state.radiator_id,
            temperature=set_temperature,
            hvac_mode=set_mode,
        )
    else:
        log.info('[%s] Turning radiator off.', climate_state.automation_id)
        climate.turn_off(entity_id=climate_state.radiator_id)
