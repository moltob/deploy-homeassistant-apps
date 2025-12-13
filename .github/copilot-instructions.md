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
- Use `this` template variable to access automation context: `"{{ this.name }}"` ([docs](https://www.home-assistant.io/docs/automation/templating/#available-state-data))
- Example:
  ```yaml
  actions:
    - action: pyscript.light_multi_switch
      data:
        automation_id: "{{ this.name }}"
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

**Class Pattern (C-style)**
- Use classes ONLY for data structures (state containers)
- Define instance variables with type hints
- Keep all methods as free functions taking the data structure as first argument
- Example:
  ```python
  class MyState:
      entity_id: str
      value: int

  def update_state(state: MyState, new_value: int):
      state.value = new_value
  ```

**Configuration vs Trigger Parameters**
- **Configuration parameters** (from `!input`): Store in state object on first initialization only
  - Examples: entity IDs, durations, thresholds
  - These define the automation's behavior and don't change across invocations
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

          # Initialize configuration parameters
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

### File Location
Place PyScript files in: `platforms/pyscript-apps/src/apps/`
