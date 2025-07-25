#!/usr/bin/env python3
"""
Project Restructure Script

This script reorganizes the project structure to follow Python packaging best practices.
"""

import os
import sys
import shutil
import argparse
from pathlib import Path


def create_directories(project_root: Path, dry_run: bool = False):
    """Create new directory structure."""
    directories = [
        "src/product_pipeline/core",
        "src/product_pipeline/notifications", 
        "src/product_pipeline/repositories",
        "src/product_pipeline/utils",
        "src/product_pipeline/stages",
        "tests/unit",
        "tests/integration",
        "config",
    ]
    
    for directory in directories:
        dir_path = project_root / directory
        print(f"Creating directory: {directory}")
        if not dry_run:
            dir_path.mkdir(parents=True, exist_ok=True)


def move_files(project_root: Path, dry_run: bool = False):
    """Move files to new locations."""
    moves = [
        # Main entry point
        ("product_pipeline.py", "src/product_pipeline/main.py"),
        
        # Core modules
        ("pipelines/pipeline.py", "src/product_pipeline/core/pipeline.py"),
        ("pipelines/__init__.py", "src/product_pipeline/core/__init__.py"),
        
        # Notifications
        ("notifications/base_channel.py", "src/product_pipeline/notifications/base.py"),
        ("notifications/email_channel.py", "src/product_pipeline/notifications/email.py"),
        ("notifications/slack_channel.py", "src/product_pipeline/notifications/slack.py"),
        ("notifications/__init__.py", "src/product_pipeline/notifications/__init__.py"),
        
        # Repositories
        ("repositories/base_repository.py", "src/product_pipeline/repositories/base.py"),
        ("repositories/artifactory.py", "src/product_pipeline/repositories/artifactory.py"),
        ("repositories/nexus.py", "src/product_pipeline/repositories/nexus.py"),
        ("repositories/s3.py", "src/product_pipeline/repositories/s3.py"),
        ("repositories/__init__.py", "src/product_pipeline/repositories/__init__.py"),
        
        # Utils
        ("utils_py/config_loader.py", "src/product_pipeline/utils/config.py"),
        ("utils_py/config_helper.py", "src/product_pipeline/utils/helpers.py"),
        ("utils_py/logger_setup.py", "src/product_pipeline/utils/logging.py"),
        ("utils_py/__init__.py", "src/product_pipeline/utils/__init__.py"),
        
        # Stages
        ("stages_placeholder/clone.py", "src/product_pipeline/stages/clone.py"),
        ("stages_placeholder/deploy.py", "src/product_pipeline/stages/deploy.py"),
        ("stages_placeholder/integration_test.py", "src/product_pipeline/stages/test.py"),
        ("stages_placeholder/notify.py", "src/product_pipeline/stages/notify.py"),
        ("stages_placeholder/__init__.py", "src/product_pipeline/stages/__init__.py"),
        
        # Tests
        ("unit_test_PyTest/test_pipeline.py", "tests/unit/test_pipeline.py"),
        ("unit_test_PyTest/test_notifications.py", "tests/unit/test_notifications.py"),
        ("unit_test_PyTest/test_repositories.py", "tests/unit/test_repositories.py"),
        ("unit_test_PyTest/test_config_loader.py", "tests/unit/test_utils.py"),
        ("unit_test_PyTest/test_product_pipeline.py", "tests/unit/test_main.py"),
        ("unit_test_PyTest/test_integration_pipeline.py", "tests/integration/test_integration.py"),
        ("unit_test_PyTest/__init__.py", "tests/__init__.py"),
        
        # Config
        ("config.yaml", "config/config.yaml"),
        ("secrets.yaml", "config/secrets.yaml"),
        ("env.example", "config/env.example"),
        
        # Version file
        ("src/__version__.py", "src/product_pipeline/__version__.py"),
    ]
    
    for src, dst in moves:
        src_path = project_root / src
        dst_path = project_root / dst
        
        if src_path.exists():
            print(f"Moving: {src} -> {dst}")
            if not dry_run:
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(src_path), str(dst_path))
        else:
            print(f"Warning: Source file not found: {src}")


def create_init_files(project_root: Path, dry_run: bool = False):
    """Create __init__.py files for new packages."""
    init_locations = [
        "src/product_pipeline",
        "tests",
    ]
    
    for location in init_locations:
        init_file = project_root / location / "__init__.py"
        if not init_file.exists():
            print(f"Creating: {location}/__init__.py")
            if not dry_run:
                init_file.touch()


def update_imports(project_root: Path, dry_run: bool = False):
    """Update import statements in Python files."""
    import_patterns = [
        ("from product_pipeline.utils.logging import", "from product_pipeline.utils.logging import"),
        ("from product_pipeline.utils.config import", "from product_pipeline.utils.config import"),
        ("from product_pipeline.utils.helpers import", "from product_pipeline.utils.helpers import"),
        ("from product_pipeline.core.pipeline import", "from product_pipeline.core.pipeline import"),
        ("from product_pipeline.notifications.", "from product_pipeline.notifications."),
        ("from product_pipeline.repositories.", "from product_pipeline.repositories."),
        ("from product_pipeline.stages.", "from product_pipeline.stages."),
    ]
    
    python_files = list(project_root.rglob("*.py"))
    
    for file_path in python_files:
        if file_path.is_file():
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                for old_import, new_import in import_patterns:
                    content = content.replace(old_import, new_import)
                
                if content != original_content:
                    print(f"Updating imports in: {file_path.relative_to(project_root)}")
                    if not dry_run:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                            
            except Exception as e:
                print(f"Error updating {file_path}: {e}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Restructure project to follow Python packaging best practices")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done without making changes")
    parser.add_argument("--project-root", type=str, default=".", help="Project root directory")
    
    args = parser.parse_args()
    
    project_root = Path(args.project_root).resolve()
    
    if not project_root.exists():
        print(f"Error: Project root does not exist: {project_root}")
        sys.exit(1)
    
    print("Starting project restructure...")
    print(f"Project root: {project_root}")
    print(f"Dry run: {args.dry_run}")
    print("-" * 50)
    
    try:
        create_directories(project_root, args.dry_run)
        move_files(project_root, args.dry_run)
        create_init_files(project_root, args.dry_run)
        update_imports(project_root, args.dry_run)
        
        print("-" * 50)
        print("Project restructure completed successfully!")
        
        if args.dry_run:
            print("This was a dry run. No changes were made.")
        else:
            print("Please review the changes and run tests to ensure everything works.")
            
    except Exception as e:
        print(f"Error during restructure: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main() 