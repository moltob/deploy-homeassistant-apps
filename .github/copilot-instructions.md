# Copilot Instructions

## PyScript Development Guidelines

### Blueprint to PyScript Integration

**Blueprint Structure**
- Blueprints define `input` parameters (switches, lights, durations, etc.)
- Use `selector` to specify input types (entity, device, number, etc.)
- For multiple entities: set `multiple: true` in selector
- Define `triggers` to specify when automation runs
- Define `actions` to call services (including PyScript services)

**Passing Data from Blueprint to PyScript**
- In blueprint `actions` section, call PyScript service: `action: pyscript.my_service`
- Pass data via `data:` block using `!input` tags to reference blueprint inputs
- Use Jinja2 templates for dynamic values from triggers: `"{{ trigger.id }}"`, `"{{ trigger.to_state.state }}"`
- Use `this` template variable to access automation context: `"{{ this.entity_id }}"` ([docs](https://www.home-assistant.io/docs/automation/templating/#available-state-data))
- Example:
  ```yaml
  actions:
    - action: pyscript.light_multi_switch
      data:
        automation_id: "{{ this.entity_id }}"
        entity_ids: !input lights
        event_id: "{{ trigger.id }}"
  ```

**PyScript Service Function Receives Data**
- Service function parameters match the keys in blueprint's `data:` block
- Single entity input → `str` (entity ID)
- Multiple entity input → `list[str]` (list of entity IDs)
- Example:
  ```python
  @service
  def light_multi_switch(automation_id: str, entity_ids: list[str], event_id: str):
      # automation_id - for state management
      # entity_ids - configuration parameter from !input lights
      # event_id - trigger parameter from {{ trigger.id }}
      pass
  ```

### Code Structure

**Service Functions**
- Use `@service` decorator for entry point functions callable from Home Assistant
- Service functions receive parameters from blueprint `data` section as keyword arguments
- Implement main logic directly in the service function
- **Argument order**: 1) automation_id, 2) configuration parameters (entity IDs, etc.), 3) trigger parameters (event_id, new_state, etc.)

**No Async/Await**
- Do NOT use `async`/`await` keywords - PyScript handles asynchronous execution implicitly
- Functions can call async operations synchronously (e.g., `light.turn_on()`, `task.sleep()`)

**PyScript Limitations**
- Do NOT use `match`/`case` statements - not supported by PyScript runtime
- Use `if`/`elif`/`else` chains instead for pattern matching

**Class Pattern (C-style)**
- Use classes ONLY for data structures (state containers)
- Define instance variables with type hints
- Always include `automation_id: str` as the first field for logging/identification
- Keep all methods as free functions taking the data structure as first argument
- Example:
  ```python
  class MyState:
      automation_id: str
      entity_id: str
      value: int

  def update_state(state: MyState, new_value: int):
      state.value = new_value
  ```

**Configuration vs Trigger Parameters**
- **Configuration parameters** (from `!input`): Store in state object on first initialization only
  - Examples: automation_id, entity IDs, durations, thresholds
  - These define the automation's behavior and don't change across invocations
  - **Always store automation_id first** for use in logging
- **Trigger parameters** (from `{{ trigger.* }}`): Pass as function arguments, do NOT store in state
  - Examples: `new_state`, `event_id`, trigger data
  - These represent dynamic events that trigger the automation
- Pattern:
  ```python
  @service
  def my_service(automation_id: str, entity_id: str, event_id: str):
      # Get or create state for this automation instance
      if not (state := state_by_instance.get(automation_id)):
          state = MyState()
          state_by_instance[automation_id] = state

          # Initialize configuration parameters (including automation_id)
          state.automation_id = automation_id
          state.entity_id = entity_id

      # Trigger: event_id - use as argument, don't store
      handle_event(state, event_id)
  ```

**State Management**
- Use module-level dictionary to track state across service calls
- Key by automation ID if available, otherwise use stable hash from input parameters
- Example: `state_by_instance: dict[str, MyState] = {}`
- For entity-based keys: `hash(tuple(sorted(entity_ids)))`

**Entry Point Pattern**
```python
@service
def my_service(param1: str, param2: int):
    # Main logic here
    pass
```

**Function Ordering**
- Order functions from public to internal based on invocation order
- Structure: 1) @service function first, 2) helper functions in the order they are called
- This makes code flow readable from top to bottom
- Example:
  ```python
  @service
  def my_service(automation_id: str, entity_id: str):
      if not (state := state_by_instance.get(automation_id)):
          initialize_state(automation_id, entity_id)

      process_action(state)

  def initialize_state(automation_id: str, entity_id: str):
      # Called first from my_service
      state = MyState()
      state.entity_id = entity_id
      state_by_instance[automation_id] = state

  def process_action(state: MyState):
      # Called second from my_service
      validate_state(state)

  def validate_state(state: MyState):
      # Called from process_action
      pass
  ```

**Logging**
- Include automation_id context in all log messages for traceability
- Use `[automation_id]` prefix format at the start of log messages
- Always store automation_id in the state object first field
- Use `state.automation_id` for all log statements
- Example:
  ```python
  log.info('[%s] Processing started.', state.automation_id)
  log.debug('[%s] Current state: %s', state.automation_id, current_state)
  log.warning('[%s] Invalid value %r received.', state.automation_id, bad_value)
  ```

### Imports and Stubs

**Import Stubs for Type Hints and Autocomplete**
- Import from `stubs.pyscript_builtins` for static PyScript built-ins (`log`, `service`, `task`)
- Import from `stubs.pyscript_generated` for Home Assistant domain services (e.g., `light`)
- These stubs provide IDE support but resolve to actual PyScript functionality at runtime

**Example Imports**
```python
from stubs.pyscript_builtins import log, service, task
from stubs.pyscript_generated import light
```

### Runtime-Adjustable Parameters

**Input Helpers (Recommended)**
- Use Home Assistant input helpers for runtime-adjustable parameters
- Pre-create input helpers in `configuration.yaml` or via UI
- Reference them in blueprint using entity selectors
- Users can modify values via dashboards
- Pattern:
  ```yaml
  # In blueprint input section:
  comfort_temp:
    name: Comfort Temperature Input
    selector:
      entity:
        domain: input_number

  # In blueprint actions:
  actions:
    - action: pyscript.my_service
      data:
        comfort_temp_id: !input comfort_temp
  ```

  ```python
  # In PyScript:
  @service
  def my_service(automation_id: str, comfort_temp_id: str, ...):
      # Read current value from input helper
      comfort_temp = float(state.get(comfort_temp_id))
  ```

**Creating Input Helpers in YAML**
- Add to `configuration.yaml` or separate included file:
  ```yaml
  input_number:
    bedroom_comfort_temp:
      name: Bedroom Comfort Temperature
      min: 15
      max: 25
      step: 0.5
      initial: 21
      unit_of_measurement: "°C"
      icon: mdi:thermometer
    bedroom_eco_temp:
      name: Bedroom Eco Temperature
      min: 10
      max: 20
      step: 0.5
      initial: 18
      unit_of_measurement: "°C"
      icon: mdi:thermometer-low

  input_datetime:
    bedroom_comfort_start:
      name: Bedroom Comfort Start Time
      has_date: false
      has_time: true
      initial: "07:00:00"
      icon: mdi:clock-start
    bedroom_comfort_stop:
      name: Bedroom Comfort Stop Time
      has_date: false
      has_time: true
      initial: "22:00:00"
      icon: mdi:clock-end
  ```

**When to Use Input Helpers**
- Runtime-adjustable parameters (temperatures, schedules, thresholds)
- Values that users change frequently via dashboards
- Parameters that need validation constraints (min/max, step)
- Want familiar HA UI configuration
