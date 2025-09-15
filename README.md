# My N8N Workflows Collection

Welcome to my collection of N8N workflows! This repository contains various automation workflows created and exported from N8N, covering different use cases and integrations.

## About N8N

N8N is an open-source workflow automation tool that allows you to connect different services and automate tasks through a visual interface. Each workflow in this repository is provided as a JSON file that can be imported directly into your N8N instance.

## How to Use These Workflows

1. **Download** the JSON file of the workflow you're interested in
2. **Open** your N8N instance
3. **Click** on "Import" in the N8N interface
4. **Upload** the JSON file or copy/paste its contents
5. **Configure** any required credentials and settings
6. **Activate** the workflow

## Workflows

<!-- WORKFLOWS_START -->
*No workflows have been added yet. Check back soon for automation workflows!*<!-- WORKFLOWS_END -->

## Adding New Workflows

To add a new workflow to this repository:

1. **Export** your workflow from N8N as a JSON file
2. **Add** the JSON file to the root directory of this repository
3. **Commit and push** your changes
4. The README.md will be **automatically updated** with your workflow information

### Automatic Documentation

This repository includes:
- **`update_readme.py`** - Script that automatically scans for workflow JSON files and updates this README
- **GitHub Actions workflow** - Automatically runs the update script when JSON files are added or modified
- **Intelligent parsing** - Extracts workflow names, descriptions, node types, and status from JSON files

### Manual Update

You can also manually update the documentation by running:
```bash
python3 update_readme.py
```

## Contributing

If you'd like to suggest improvements to any workflow or report issues:

1. Open an issue describing the problem or suggestion
2. For workflow modifications, please test thoroughly before suggesting changes

## Structure

Each workflow JSON file in this repository follows the standard N8N export format and includes:
- Workflow nodes and connections
- Node configurations (excluding sensitive credentials)
- Trigger and execution settings
- Workflow metadata

## Requirements

- N8N instance (self-hosted or cloud)
- Appropriate credentials for services used in workflows
- Basic understanding of the workflow's purpose and configuration

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Last updated: 2025-09-15 20:43:01 UTC*