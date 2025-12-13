# AppDaemon Migration Plan

## Motivation

Migrate away from AppDaemon due to platform instability and maintenance burden:

- **Instability**: Breaking changes to automations ~2x per year
- **Async Support**: Possible but poorly supported despite AD being fully async
- **Code Quality**: Non-pythonic and quirky codebase
- **Track Record**: Multiple issues encountered ([see GitHub issues](https://github.com/AppDaemon/appdaemon/issues?q=is%3Aissue%20state%3Aopen%20commenter%3Amoltob))

## Migration Target Platforms

Evaluate the following alternatives:

1. **[Home Assistant's `python_script`](https://www.home-assistant.io/integrations/python_script/)** - Built-in Python scripting
2. **[PythonScriptsPro](https://github.com/AlexxIT/PythonScriptsPro)** - Extended Python scripts integration
3. **[`pyscript` Integration](https://hacs-pyscript.readthedocs.io/)** - Full-featured Python automation platform

## Migration Phases

### Phase 1: Audit Current State

- [ ] Analyze which automations are actively running in HA instance
- [ ] Identify dead/unused automations
- [ ] Delete unused automations and entities

### Phase 2: Automation Assessment

For each automation still in use:

- [ ] Can this be implemented with HA's native mechanisms?
- [ ] Are blueprints viable?
  - Existing blueprints suitable?
  - Worth creating custom blueprints for reusability?
- [ ] If Python is required, document needs:
  - Async support (e.g., for non-blocking delays)
  - Local state management within logic
  - Other Python features

### Phase 3: Platform Evaluation

Once Python requirements are clear:

- [ ] Review candidate platform documentation against feature requirements
- [ ] Create proof-of-concept implementations
- [ ] Compare platforms on:
  - Feature completeness
  - Stability and maintenance
  - Community support
  - Migration effort

### Phase 4: Implementation

- [ ] Select target platform
- [ ] Migrate automations incrementally
- [ ] Test each migration thoroughly
- [ ] Decommission AppDaemon infrastructure
