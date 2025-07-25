#!/usr/bin/env python3
"""
Fix naming conventions according to Python best practices.
"""

import os
import shutil
from pathlib import Path


def remove_old_directories():
    """Remove old directories that are no longer needed."""
    old_dirs = [
        "unit_test_PyTest",
        "stages_placeholder", 
        "utils_py",
        "notifications",
        "repositories",
        "pipelines",
    ]
    
    for dir_name in old_dirs:
        dir_path = Path(dir_name)
        if dir_path.exists() and dir_path.is_dir():
            print(f"Removing old directory: {dir_name}")
            try:
                shutil.rmtree(dir_path)
            except Exception as e:
                print(f"Error removing {dir_name}: {e}")


def remove_duplicate_files():
    """Remove duplicate and outdated files."""
    files_to_remove = [
        "Readme.md",  # Duplicate of README.md
        "architecture.txt",  # Outdated
        "user_guide.md",  # Outdated
    ]
    
    for file_name in files_to_remove:
        file_path = Path(file_name)
        if file_path.exists():
            print(f"Removing file: {file_name}")
            try:
                file_path.unlink()
            except Exception as e:
                print(f"Error removing {file_name}: {e}")


def check_src_naming_conventions():
    """Check naming conventions in src/ directory."""
    src_path = Path("src")
    if not src_path.exists():
        print("src/ directory not found!")
        return
    
    issues = []
    
    # Check all Python files and directories in src/
    for item in src_path.rglob("*"):
        if item.is_file() and item.suffix == ".py":
            # Check file naming (should be snake_case)
            if not is_snake_case(item.stem):
                issues.append(f"File should use snake_case: {item}")
        
        elif item.is_dir() and item.name != "__pycache__":
            # Check directory naming (should be snake_case)
            if not is_snake_case(item.name):
                issues.append(f"Directory should use snake_case: {item}")
    
    if issues:
        print("Naming convention issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("✅ All naming conventions in src/ are correct!")


def is_snake_case(name):
    """Check if a name follows snake_case convention."""
    if not name:
        return True
    
    # Allow special names like __init__, __version__, etc.
    if name.startswith("__") and name.endswith("__"):
        return True
    
    # Check for snake_case pattern
    import re
    return bool(re.match(r'^[a-z][a-z0-9_]*$', name))


def check_file_permissions():
    """Check and fix file permissions."""
    # Make scripts executable
    scripts = [
        "scripts/restructure_project.py",
        "scripts/fix_imports.py",
        "scripts/fix_naming_conventions.py",
    ]
    
    for script in scripts:
        script_path = Path(script)
        if script_path.exists():
            try:
                script_path.chmod(0o755)
                print(f"Made executable: {script}")
            except Exception as e:
                print(f"Error making {script} executable: {e}")


def create_cleanup_script():
    """Create a cleanup script for future use."""
    cleanup_script = """#!/usr/bin/env python3
\"\"\"
Cleanup script for removing temporary files and caches.
\"\"\"

import shutil
from pathlib import Path

def cleanup():
    \"\"\"Remove temporary files and caches.\"\"\"
    items_to_remove = [
        "__pycache__",
        ".pytest_cache",
        ".mypy_cache",
        "*.pyc",
        "*.pyo",
        "*.pyd",
        ".coverage",
        "htmlcov",
        "bandit-report.json",
        "*.egg-info",
        "build",
        "dist",
    ]
    
    for pattern in items_to_remove:
        if pattern.startswith("*"):
            # Handle file patterns
            for file_path in Path(".").glob(pattern):
                if file_path.is_file():
                    print(f"Removing: {file_path}")
                    file_path.unlink()
        else:
            # Handle directory patterns
            for dir_path in Path(".").rglob(pattern):
                if dir_path.is_dir():
                    print(f"Removing: {dir_path}")
                    shutil.rmtree(dir_path)

if __name__ == "__main__":
    cleanup()
"""
    
    cleanup_path = Path("scripts/cleanup.py")
    cleanup_path.write_text(cleanup_script, encoding="utf-8")
    cleanup_path.chmod(0o755)
    print("Created: scripts/cleanup.py")


def main():
    """Main function."""
    print("🔍 Checking and fixing naming conventions...")
    print("=" * 50)
    
    # Remove old directories
    print("\n1. Removing old directories...")
    remove_old_directories()
    
    # Remove duplicate files
    print("\n2. Removing duplicate and outdated files...")
    remove_duplicate_files()
    
    # Check src naming conventions
    print("\n3. Checking src/ naming conventions...")
    check_src_naming_conventions()
    
    # Fix file permissions
    print("\n4. Fixing file permissions...")
    check_file_permissions()
    
    # Create cleanup script
    print("\n5. Creating cleanup script...")
    create_cleanup_script()
    
    print("\n" + "=" * 50)
    print("✅ Naming conventions check completed!")
    print("\nNext steps:")
    print("1. Review the changes")
    print("2. Run tests to ensure everything works")
    print("3. Commit the changes")


if __name__ == "__main__":
    main() 