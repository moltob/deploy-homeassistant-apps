# AppDaemon Custom Applications (Ansible Deployment)

This project contains custom AppDaemon applications and configuration deployed to an existing Home Assistant AppDaemon add-on via Ansible.

## Project Structure

```
config-ansible/
├── ansible/                # Ansible deployment configuration
│   ├── inventory/          # Environment-specific inventories
│   │   └── prod/           # Production inventory
│   ├── roles/              # Ansible roles
│   │   └── appdaemon/      # AppDaemon deployment role
│   │       ├── files/      # Static files for deployment
│   │       ├── handlers/   # Restart handlers
│   │       └── tasks/      # Deployment tasks
│   └── playbooks/          # Deployment playbooks
├── src/                    # Source code
│   ├── appdaemon.yaml      # Local AppDaemon config (gitignored)
│   └── apps/               # AppDaemon Python applications
│       ├── bindings/       # Device control bindings
│       ├── network/        # Network-related apps
│       ├── sensors/        # Sensor apps
│       └── util/           # Utility modules
├── pyproject.toml          # Python project configuration
├── uv.lock                 # uv package lock file
├── run-all-checks.sh       # Development checks script
└── README.md               # This file
```

## Prerequisites

### Local Machine
- Ansible installed (`ansible-core` >= 2.14 recommended)
- SSH access to Home Assistant server
- SSH key added to SSH agent
- `ansible.posix` collection: `ansible-galaxy collection install ansible.posix`

### Home Assistant
**AppDaemon Add-on:**
- The AppDaemon add-on must be installed and running
- Note: This project deploys custom applications to the existing add-on, not the add-on itself

**Advanced SSH & Web Terminal Add-on:**
The "Advanced SSH & Web Terminal" add-on must be installed and configured:
1. Install the add-on from the Add-on Store
2. Configure in the add-on UI:
   - **authorized_keys**: Add your SSH public key
   - **share_sessions**: Set to `false` (recommended)
   - **safe_mode**: Set to `off` (required for `ha` CLI commands)
   - **sftp**: Set to `true` (required for Ansible file transfers)
3. Start the add-on

## Local Development Configuration

For local development, you need two configuration files in the `src/` directory:

- **`src/appdaemon.yaml`** - Local AppDaemon configuration (gitignored)
- **`src/secrets.yaml`** - Global secrets file managed outside this project (gitignored)

These files should be configured with your local environment settings. The `secrets.yaml` is a global AppDaemon file shared across all projects/apps and should contain the credentials referenced in your apps.

**Tip:** Use [direnv](https://direnv.net/) with a `.envrc` file to automatically load environment variables for local development.

## Deployment

### Run Deployment

The deployment copies `ansible/roles/appdaemon/files/appdaemon.yaml` to production and syncs the `src/apps/` directory. No templating or environment variables are used during deployment.

**Note:** `secrets.yaml` is NOT deployed by this playbook - it's managed globally on the target system.

#### Check Mode (Dry Run)
```bash
cd config-ansible
ansible-playbook -i ansible/inventory/prod ansible/playbooks/deploy.yml --check --diff
```

#### Full Deployment
```bash
cd config-ansible
ansible-playbook -i ansible/inventory/prod ansible/playbooks/deploy.yml
```

### Verify Deployment

After deployment completes:
1. Check AppDaemon logs in Home Assistant: Settings → Add-ons → AppDaemon → Log
2. Verify all apps loaded successfully
3. Test automation functionality

## Development

This project includes all development tooling:
- `pyproject.toml` - Python project configuration
- `uv.lock` - uv package lock file
- `renovate.json5` - Automated dependency updates
- `run-all-checks.sh` - Run all code quality checks

Development files are automatically excluded from deployment to production.

## Deployment Details

- **What is deployed**:
  - `appdaemon.yaml` configuration file (from `ansible/roles/appdaemon/files/`)
  - Custom AppDaemon applications from `src/apps/` directory
- **What is NOT deployed**:
  - `secrets.yaml` (managed globally on target system)
  - Development files (pyproject.toml, uv.lock, renovate.json5, run-all-checks.sh, etc.)
- **Target Path**: Configured in inventory (`addon_configs_path` + `appdaemon_addon_slug`)
- **Target Host**: Configured in inventory
- **Method**: SSH-based Ansible deployment
- **Restart**: Automatic restart of AppDaemon add-on via `ha addons restart` command

## Troubleshooting

### SSH Connection Issues
- Verify SSH key is loaded: `ssh-add -l`
- Test manual connection: `ssh root@ha.mpagel.de`
- Check "Advanced SSH & Web Terminal" add-on is running
- Variables must be exported before running playbook

### Deployment Failures
- Run with verbose output: `ansible-playbook ... -vv`
- Check AppDaemon add-on logs for errors
- Verify file permissions on target system

## Migration Note

This project replaces the older `config` project which used Git-based deployment. The `config-ansible` project is self-contained with all necessary code and Ansible configuration for deployment.
