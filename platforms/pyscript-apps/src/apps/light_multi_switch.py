from stubs.pyscript_builtins import log, service, state
from stubs.pyscript_generated import light


class MultiSwitchState:
    entity_ids: list[str]


state_by_instance: dict[str, MultiSwitchState] = {}


def get_first_on_index(switch_state: MultiSwitchState) -> int | None:
    """Get the index of the first light that is on, or None if all are off."""
    for index, entity_id in enumerate(switch_state.entity_ids):
        if state.get(entity_id) == 'on':
            return index
    return None


def handle_single_click(state: MultiSwitchState):
    """Turn off all lights except the next one in sequence."""
    current_index = get_first_on_index(state)

    if current_index is None:
        # All off, turn on first light
        next_index = 0
    else:
        # Turn to next light (wrap around)
        next_index = (current_index + 1) % len(state.entity_ids)

    next_entity_id = state.entity_ids[next_index]

    # Turn off all lights
    log.info('Single click: switching to %r.', next_entity_id)
    for index, entity_id in enumerate(state.entity_ids):
        if index == next_index:
            light.turn_on(entity_id=entity_id)
        else:
            light.turn_off(entity_id=entity_id)


def handle_double_click(state: MultiSwitchState):
    """Toggle all lights on or off together."""
    current_index = get_first_on_index(state)

    if current_index is None:
        # All off, turn all on
        log.info('Double click: turning on all lights.')
        for entity_id in state.entity_ids:
            light.turn_on(entity_id=entity_id)
    else:
        # At least one on, turn all off
        log.info('Double click: turning off all lights.')
        for entity_id in state.entity_ids:
            light.turn_off(entity_id=entity_id)


@service
def light_multi_switch(automation_id: str, entity_ids: list[str], event_id: str):
    # Get or create state for this automation instance with configuration parameters
    if not (state := state_by_instance.get(automation_id)):
        log.info('Initializing for automation %r with %d lights.', automation_id, len(entity_ids))
        state = MultiSwitchState()
        state_by_instance[automation_id] = state

        state.entity_ids = entity_ids

    # Process trigger parameter (event_id)
    log.info('Processing event %r for automation %r.', event_id, automation_id)
    if event_id == 'single':
        handle_single_click(state)
    elif event_id == 'double':
        handle_double_click(state)
    else:
        log.warning('Unknown event_id %r, ignoring.', event_id)
