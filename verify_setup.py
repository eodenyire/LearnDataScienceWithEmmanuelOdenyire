#!/usr/bin/env python3
"""
Setup Verification Script for Data Science Bootcamp

This script verifies that your environment is set up correctly for the bootcamp.
"""

import sys
import importlib

def check_python_version():
    """Check if Python version is 3.8 or higher."""
    print("Checking Python version...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 8:
        print(f"✓ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"✗ Python {version.major}.{version.minor}.{version.micro} - Please upgrade to Python 3.8+")
        return False

def check_package(package_name, display_name=None):
    """Check if a package is installed and display its version."""
    if display_name is None:
        display_name = package_name
    
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'unknown')
        print(f"✓ {display_name} ({version}) - OK")
        return True
    except ImportError:
        print(f"✗ {display_name} - NOT INSTALLED")
        return False

def main():
    """Run all verification checks."""
    print("=" * 60)
    print("Data Science Bootcamp - Environment Verification")
    print("=" * 60)
    print()
    
    all_ok = True
    
    # Check Python version
    all_ok &= check_python_version()
    print()
    
    # Check essential packages
    print("Checking essential packages...")
    packages = [
        ('numpy', 'NumPy'),
        ('pandas', 'Pandas'),
        ('matplotlib', 'Matplotlib'),
        ('seaborn', 'Seaborn'),
        ('sklearn', 'scikit-learn'),
        ('scipy', 'SciPy')
    ]
    
    for pkg, name in packages:
        all_ok &= check_package(pkg, name)
    
    print()
    
    # Check optional packages
    print("Checking optional packages (for later months)...")
    optional_packages = [
        ('tensorflow', 'TensorFlow'),
        ('torch', 'PyTorch'),
        ('nltk', 'NLTK'),
        ('flask', 'Flask'),
        ('streamlit', 'Streamlit')
    ]
    
    for pkg, name in optional_packages:
        check_package(pkg, name)
    
    print()
    print("=" * 60)
    
    if all_ok:
        print("✓ Your environment is ready for the bootcamp!")
        print("Run 'jupyter notebook' to get started.")
    else:
        print("✗ Some required packages are missing.")
        print("Run 'pip install -r requirements.txt' to install them.")
    
    print("=" * 60)
    
    return 0 if all_ok else 1

if __name__ == "__main__":
    sys.exit(main())
