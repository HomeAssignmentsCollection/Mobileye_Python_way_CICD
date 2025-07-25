#!/usr/bin/env python3
"""
Cleanup script for removing temporary files and caches.
"""

import shutil
from pathlib import Path

def cleanup():
    """Remove temporary files and caches."""
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
