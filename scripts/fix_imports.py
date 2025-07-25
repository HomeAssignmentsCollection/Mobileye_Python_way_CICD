#!/usr/bin/env python3
"""
Fix imports after project restructure.
"""

import os
import re
from pathlib import Path


def fix_imports_in_file(file_path: Path) -> None:
    """Fix imports in a single file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Fix base_repository imports
        content = re.sub(
            r'from product_pipeline\.repositories\.base_repository import',
            'from product_pipeline.repositories.base import',
            content
        )
        
        # Fix email_channel imports
        content = re.sub(
            r'from product_pipeline\.notifications\.email_channel import',
            'from product_pipeline.notifications.email import',
            content
        )
        
        # Fix slack_channel imports
        content = re.sub(
            r'from product_pipeline\.notifications\.slack_channel import',
            'from product_pipeline.notifications.slack import',
            content
        )
        
        # Fix base_channel imports
        content = re.sub(
            r'from product_pipeline\.notifications\.base_channel import',
            'from product_pipeline.notifications.base import',
            content
        )
        
        if content != original_content:
            print(f"Fixing imports in: {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
    except Exception as e:
        print(f"Error fixing {file_path}: {e}")


def main():
    """Main function."""
    project_root = Path(".")
    
    # Find all Python files
    python_files = list(project_root.rglob("*.py"))
    
    for file_path in python_files:
        if file_path.is_file():
            fix_imports_in_file(file_path)
    
    print("Import fixes completed!")


if __name__ == "__main__":
    main() 