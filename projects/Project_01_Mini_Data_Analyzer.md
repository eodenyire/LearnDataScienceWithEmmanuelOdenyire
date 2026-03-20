# Project 01: Mini Data Analyzer

## Overview
Build a Python command-line tool that performs statistical analysis on any CSV file.

## Learning Outcomes
- Apply Python OOP and functional programming
- Practice file I/O and data structures
- Build a reusable, modular tool

## Minimum Requirements
1. Load and validate a CSV file
2. Auto-detect numerical vs categorical columns
3. Compute summary statistics for numerical columns
4. Show value counts for categorical columns
5. Report missing values
6. Save analysis as JSON report

## Suggested Architecture
```python
DataAnalyzer
├── load(filepath) -> DataFrame
├── describe_numerical(col) -> dict
├── describe_categorical(col) -> dict
├── missing_summary() -> dict
└── generate_report(output_path)
```

## Dataset Suggestions
- Titanic (`datasets/titanic.csv`)
- Student exam scores
- Weather data

## Deliverables
- `analyzer.py` script
- Sample output report
- GitHub README with usage instructions

## Extension Ideas
- Interactive CLI with `rich` library
- Export to HTML report
- Add visualization with matplotlib
