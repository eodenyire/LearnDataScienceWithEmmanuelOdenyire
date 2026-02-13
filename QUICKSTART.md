# Quick Start Guide

Get started with the Data Science Bootcamp in 5 minutes!

## Prerequisites

- Python 3.8 or higher installed
- pip (Python package manager)
- Git (for cloning the repository)

## Installation Steps

### 1. Clone the Repository
```bash
git clone https://github.com/eodenyire/LearnDataScienceWithEmmanuelOdenyire.git
cd LearnDataScienceWithEmmanuelOdenyire
```

### 2. (Optional) Create a Virtual Environment
It's recommended to use a virtual environment to avoid conflicts:

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Packages
```bash
pip install -r requirements.txt
```

This may take a few minutes as it installs all necessary packages.

### 4. Verify Installation
```bash
python verify_setup.py
```

You should see checkmarks (✓) for all essential packages.

### 5. Start Jupyter Notebook
```bash
jupyter notebook
```

This will open Jupyter in your web browser.

### 6. Begin Learning!
Navigate to `Month_01_Python_Basics` and open:
- `Day_01_Introduction_to_Data_Science_and_Python.ipynb`

## Troubleshooting

### Package Installation Issues

If you encounter errors during package installation:

1. **Update pip:**
   ```bash
   pip install --upgrade pip
   ```

2. **Install packages one by one:**
   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn
   ```

3. **For TensorFlow/PyTorch issues:**
   These are optional for Month 1. You can install them later:
   ```bash
   # Skip for now, install when needed in Month 9
   ```

### Jupyter Notebook Not Opening

1. **Check if Jupyter is installed:**
   ```bash
   jupyter --version
   ```

2. **Try JupyterLab instead:**
   ```bash
   jupyter lab
   ```

3. **Specify browser manually:**
   ```bash
   jupyter notebook --browser=firefox
   ```

### Import Errors in Notebooks

If you get import errors when running notebook cells:

1. Make sure your virtual environment is activated (if using one)
2. Restart the Jupyter kernel: `Kernel > Restart`
3. Re-run the verification script: `python verify_setup.py`

## What's Next?

1. **Complete Month 1** - Focus on Python basics
2. **Practice Daily** - Consistency is key
3. **Join the Community** - See CONTRIBUTING.md for ways to engage
4. **Work on Projects** - Apply what you learn

## Learning Tips

- **Don't rush** - Take time to understand each concept
- **Practice coding** - Don't just read, write code!
- **Ask questions** - Use GitHub issues for questions
- **Join discussions** - Learn from others
- **Build projects** - Apply skills to real problems

## Resources

- [Main README](README.md) - Complete documentation
- [Contributing Guide](CONTRIBUTING.md) - How to contribute
- [Resources Directory](resources/README.md) - Additional learning materials

## Need Help?

- Check the [Resources](resources/README.md) directory
- Open an issue on GitHub
- Review the troubleshooting section above

Happy Learning! 🎉
