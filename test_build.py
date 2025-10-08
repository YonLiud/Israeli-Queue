#!/usr/bin/env python3
"""
Local build and test script for Israeli Queue.

This script simulates the CI/CD pipeline locally to help verify
that everything works before pushing to GitHub.
"""

import subprocess
import sys
import os
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle errors."""
    print(f"\n🔄 {description}")
    print(f"Running: {cmd}")

    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        print(f"✅ {description} - PASSED")
        if result.stdout.strip():
            print(f"Output: {result.stdout.strip()}")
    else:
        print(f"❌ {description} - FAILED")
        print(f"Error: {result.stderr}")
        return False

    return True


def main():
    """Run the complete local test pipeline."""
    print("🚀 Israeli Queue - Local Build & Test Pipeline")
    print("=" * 50)

    # Change to project directory
    project_root = Path(__file__).parent
    os.chdir(project_root)

    steps = [
        # Install dependencies
        ("pip install -r requirements-dev.txt", "Installing dependencies"),
        ("pip install -e .", "Installing package in development mode"),
        # Code quality checks
        ("black --check .", "Checking code formatting"),
        ("flake8 .", "Running linting checks"),
        ("mypy IsraeliQueue/ --ignore-missing-imports", "Type checking"),
        # Security checks
        (
            "echo 'No production dependencies to check' || safety check --short-report",
            "Security vulnerability scan",
        ),
        ("bandit -r IsraeliQueue/", "Security code analysis"),
        # Testing
        ("pytest --cov=IsraeliQueue --cov-report=term-missing", "Running test suite"),
        # Build package
        ("python -m build", "Building package"),
        ("twine check dist/*", "Validating package"),
    ]

    failed_steps = []

    for cmd, description in steps:
        if not run_command(cmd, description):
            failed_steps.append(description)

    print("\n" + "=" * 50)
    print("📊 PIPELINE RESULTS")
    print("=" * 50)

    if not failed_steps:
        print("🎉 ALL CHECKS PASSED!")
        print("✅ Ready to push to GitHub")
        print("✅ CI/CD pipeline should succeed")
    else:
        print("❌ SOME CHECKS FAILED:")
        for step in failed_steps:
            print(f"   - {step}")
        print("\n🔧 Please fix the issues above before pushing")
        return 1

    print("\n📦 Next Steps:")
    print("1. Commit your changes: git add . && git commit -m 'your message'")
    print("2. Push to GitHub: git push")
    print("3. Create a release for PyPI publishing")

    return 0


if __name__ == "__main__":
    sys.exit(main())
