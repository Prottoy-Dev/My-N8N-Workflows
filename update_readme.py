#!/usr/bin/env python3
"""
Script to automatically update README.md with workflow descriptions
based on JSON workflow files in the repository.
"""

import json
import os
import re
from datetime import datetime
from pathlib import Path


def extract_workflow_info(json_file_path):
    """Extract workflow information from N8N JSON file."""
    try:
        with open(json_file_path, 'r', encoding='utf-8') as f:
            workflow_data = json.load(f)
        
        # Extract basic workflow information
        info = {
            'filename': os.path.basename(json_file_path),
            'name': workflow_data.get('name', 'Unnamed Workflow'),
            'description': '',
            'nodes': [],
            'created_at': workflow_data.get('createdAt', ''),
            'updated_at': workflow_data.get('updatedAt', ''),
            'active': workflow_data.get('active', False)
        }
        
        # Try to extract description from workflow settings or meta
        if 'settings' in workflow_data and 'description' in workflow_data['settings']:
            info['description'] = workflow_data['settings']['description']
        elif 'meta' in workflow_data and 'description' in workflow_data['meta']:
            info['description'] = workflow_data['meta']['description']
        
        # Extract node types to understand workflow functionality
        if 'nodes' in workflow_data:
            node_types = set()
            for node in workflow_data['nodes']:
                if 'type' in node:
                    node_types.add(node['type'])
            info['nodes'] = sorted(list(node_types))
        
        return info
    
    except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
        print(f"Error processing {json_file_path}: {e}")
        return None


def generate_workflow_section(workflows):
    """Generate the workflows section for README.md."""
    if not workflows:
        return "*No workflows have been added yet. Check back soon for automation workflows!*"
    
    sections = []
    
    for workflow in sorted(workflows, key=lambda x: x['name'].lower()):
        section = f"### {workflow['name']}\n\n"
        section += f"**File:** `{workflow['filename']}`\n\n"
        
        if workflow['description']:
            section += f"**Description:** {workflow['description']}\n\n"
        else:
            section += f"**Description:** *No description provided*\n\n"
        
        if workflow['nodes']:
            section += f"**Key Integrations:** {', '.join(workflow['nodes'])}\n\n"
        
        if workflow['active']:
            section += "**Status:** ✅ Active\n\n"
        else:
            section += "**Status:** ⏸️ Inactive\n\n"
        
        section += "---\n\n"
        sections.append(section)
    
    return "".join(sections)


def update_readme():
    """Update README.md with current workflow information."""
    repo_root = Path(__file__).parent
    readme_path = repo_root / "README.md"
    
    # Find all JSON files in the repository
    json_files = list(repo_root.glob("*.json"))
    json_files.extend(list(repo_root.glob("workflows/*.json")))  # Also check workflows subdirectory
    
    # Extract workflow information
    workflows = []
    for json_file in json_files:
        workflow_info = extract_workflow_info(json_file)
        if workflow_info:
            workflows.append(workflow_info)
    
    # Read current README.md
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    except FileNotFoundError:
        print("README.md not found!")
        return False
    
    # Generate new workflows section
    workflows_section = generate_workflow_section(workflows)
    
    # Update README.md content
    # Replace content between <!-- WORKFLOWS_START --> and <!-- WORKFLOWS_END -->
    pattern = r'(<!-- WORKFLOWS_START -->)(.*?)(<!-- WORKFLOWS_END -->)'
    replacement = f'\\1\n{workflows_section}\\3'
    
    new_content = re.sub(pattern, replacement, readme_content, flags=re.DOTALL)
    
    # Update timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    new_content = new_content.replace(
        "*Last updated: [Auto-generated timestamp will go here]*",
        f"*Last updated: {timestamp}*"
    )
    
    # Write updated README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"README.md updated successfully! Found {len(workflows)} workflows.")
    return True


if __name__ == "__main__":
    update_readme()