# CSV Viewer Python

[![PyPI Version](https://img.shields.io/pypi/v/csv-viewer-python?style=flat-square)](https://pypi.org/project/csv-viewer-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/csv-viewer-python?style=flat-square)](https://pypi.org/project/csv-viewer-python/)
[![License](https://img.shields.io/pypi/l/csv-viewer-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/csv-viewer-python?style=flat-square)](https://pypi.org/project/csv-viewer-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/csv-viewer-python?style=flat-square)](https://github.com/mizoz/csv-viewer-python)

> A Python CLI tool for viewing and analyzing CSV files in the terminal.

## Features

- View CSV files in terminal
- Sort by columns
- Filter data
- Search within CSV
- Export to different formats
- Python API for integration

## Installation

### From PyPI

```bash
pip install csv-viewer-python
```

### From Source

```bash
git clone https://github.com/mizoz/csv-viewer-python.git
cd csv-viewer-python
pip install -e .
```

## Usage

### Command Line

```bash
# View CSV file
csv-viewer data.csv

# Sort by column
csv-viewer data.csv --sort name

# Filter data
csv-viewer data.csv --filter "age>25"

# Search
csv-viewer data.csv --search "John"
```

### Python API

```python
from csv_viewer import CSVViewer

viewer = CSVViewer("data.csv")

# View data
data = viewer.read()
print(data)

# Sort
sorted_data = viewer.sort("name")
```

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!
