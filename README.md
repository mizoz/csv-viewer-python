# CSV Viewer Python

A lightweight command-line tool for viewing and analyzing CSV files in the terminal.

## Features

- View CSV files in a formatted table
- Display row count and column information
- Filter and sort capabilities
- Support for various CSV delimiters
- Pretty printing for terminal output

## Installation

```bash
pip install csv-viewer-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/csv-viewer-python.git
cd csv-viewer-python
pip install -e .
```

## Usage

```bash
# View a CSV file
csvviewer data.csv

# Specify delimiter
csvviewer data.csv --delimiter ","

# Show only first N rows
csvviewer data.csv --head 10

# Show column statistics
csvviewer data.csv --stats
```

## Examples

```python
from csv_viewer import CSVViewer

# View a CSV file
viewer = CSVViewer('data.csv')
viewer.display()

# Display with statistics
viewer.display_stats()
```

## Requirements

- Python 3.7+
- pandas (optional, for enhanced features)

## License

MIT License

## Author

mizoz