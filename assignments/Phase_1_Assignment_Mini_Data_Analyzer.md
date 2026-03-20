# Phase 1 Assignment: Mini Data Analyzer

## Objective
Build a command-line Python tool that analyzes a CSV dataset and generates a report.

## Requirements

### Functional Requirements
Your `data_analyzer.py` script must:
1. Accept a CSV file path as command-line argument
2. Load the file and detect column types (numerical vs categorical)
3. For **numerical columns**: mean, median, std, min, max, 25th/75th percentile
4. For **categorical columns**: unique count, top 3 values and their frequencies
5. Detect and report missing values per column
6. Save a JSON report to `output/report.json`
7. Print a formatted summary to the console

### Technical Requirements
- Use only the Python standard library + `pandas` + `numpy`
- Implement at least one class with methods
- Include type hints and docstrings
- Handle errors gracefully (missing file, wrong format)

### Bonus (10 extra points)
- Add a `--plot` flag that saves histogram plots for numerical columns
- Add unit tests using `pytest`

## Dataset Options
Use any of:
1. `datasets/titanic.csv` from this repo
2. A public dataset from Kaggle (credit: cite it in your README)
3. Any CSV with at least 500 rows and 5 columns

## Deliverables
```
mini-data-analyzer/
├── data_analyzer.py    # Main script
├── utils.py            # Helper functions (optional)
├── requirements.txt    # Dependencies
├── README.md           # How to run the script
├── output/             # Generated reports (gitignored)
└── tests/              # Bonus: unit tests
```

## Evaluation Criteria
| Criterion | Points |
|-----------|--------|
| Correct statistical calculations | 30 |
| Clean, well-structured code | 25 |
| Error handling | 15 |
| Documentation (docstrings + README) | 15 |
| JSON report output | 15 |
| **Total** | **100** |
