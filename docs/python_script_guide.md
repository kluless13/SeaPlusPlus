# Guide to Writing Python Scripts

This guide provides best practices and conventions for writing Python scripts, especially for scientific computing and data analysis.

## 1. Basic Script Structure

```python
#!/usr/bin/env python3
"""
Script Name: example_script.py
Description: Brief description of what the script does.
Author: Your Name
Date: YYYY-MM-DD
"""

# Import statements
import numpy as np
import pandas as pd

# Constants and configurations
DATA_PATH = "path/to/data"
MAX_ITERATIONS = 1000

def main_function():
    """Main function that runs the script's primary logic."""
    pass

if __name__ == "__main__":
    main_function()
```

## 2. Best Practices

### 2.1 Imports
- Group imports in the following order:
  1. Standard library imports
  2. Third-party library imports
  3. Local/custom module imports
- Use explicit imports (e.g., `from module import specific_function`)
- Avoid `from module import *`

### 2.2 Documentation
- Include a docstring at the start of the script
- Document functions using docstrings:
```python
def analyze_data(data: pd.DataFrame, threshold: float = 0.05) -> dict:
    """
    Analyze time series data for patterns.

    Parameters
    ----------
    data : pd.DataFrame
        Input data to analyze
    threshold : float, optional
        Significance threshold (default: 0.05)

    Returns
    -------
    dict
        Dictionary containing analysis results
    """
    pass
```

### 2.3 Function Design
- Write small, focused functions (single responsibility principle)
- Use type hints for better code clarity
- Return values instead of modifying data in place
- Handle errors with try-except blocks

### 2.4 Variable Naming
- Use descriptive names (e.g., `temperature_data` not `td`)
- Constants in UPPER_CASE
- Functions and variables in snake_case
- Classes in CamelCase

## 3. Error Handling

```python
def read_data(file_path: str) -> pd.DataFrame:
    """Read data from file with error handling."""
    try:
        data = pd.read_csv(file_path)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        raise
    except pd.errors.EmptyDataError:
        print("Error: File is empty")
        raise
```

## 4. Command Line Arguments

```python
import argparse

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--threshold", type=float, default=0.05,
                       help="Analysis threshold")
    return parser.parse_args()
```

## 5. Logging

```python
import logging

def setup_logging():
    """Configure logging for the script."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
# Usage
logging.info("Starting analysis...")
logging.error("An error occurred")
```

## 6. Testing

- Write unit tests for your functions
- Use pytest for testing
- Keep tests in a separate directory
- Name test files with `test_` prefix

```python
# test_analysis.py
def test_analyze_data():
    """Test the analyze_data function."""
    test_data = pd.DataFrame({"values": [1, 2, 3]})
    result = analyze_data(test_data)
    assert isinstance(result, dict)
    assert "mean" in result
```

## 7. Performance Considerations

- Use NumPy for numerical operations
- Avoid loops when vectorized operations are possible
- Profile code to identify bottlenecks
- Use generators for large datasets

## 8. Code Organization

```
project/
├── data/
├── scripts/
│   ├── analysis.py
│   └── utils.py
├── tests/
│   └── test_analysis.py
├── requirements.txt
└── README.md
```

## 9. Version Control

- Use meaningful commit messages
- Create a .gitignore file
- Don't commit sensitive data or large files
- Use branches for new features

## 10. Running Scripts

```bash
# Basic execution
python script.py

# With arguments
python script.py --input data.csv --threshold 0.01

# With Python environment
conda activate env_name
python script.py
```

## 11. Common Pitfalls to Avoid

1. Not handling file paths properly
2. Hardcoding values that should be parameters
3. Not handling missing data
4. Insufficient error handling
5. Poor documentation
6. Not using version control
7. Not following PEP 8 style guide

## 12. Additional Resources

- [PEP 8 Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Python Documentation](https://docs.python.org/3/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/) 