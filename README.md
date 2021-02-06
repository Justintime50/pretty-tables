<div align="center">

# Pretty Tables

Create pretty tables from headers and rows, perfect for console output.

[![Build Status](https://github.com/Justintime50/pretty-tables/workflows/build/badge.svg)](https://github.com/Justintime50/pretty-tables/actions)
[![Coverage Status](https://coveralls.io/repos/github/Justintime50/pretty-tables/badge.svg?branch=main)](https://coveralls.io/github/Justintime50/pretty-tables?branch=main)
[![PyPi](https://img.shields.io/pypi/v/pretty-tables)](https://pypi.org/project/pretty-tables/)
[![Licence](https://img.shields.io/github/license/justintime50/pretty-tables)](LICENSE)

<img src="assets/showcase.png" alt="Showcase">

</div>

Pretty Tables will create uniformly dispersed columns based on the input given and can be scaled to your needs in length of the table or number of columns. The input is automatically validated and converted to strings before returning successfully. Here is a simple sample output:

```
| ID | Name   | Occupation        | Employed |
| 1  | Justin | Software Engineer | True     |
| 2  | Misty  | Receptionist      | False    |
| 3  | John   | No data           | False    |
```

## Install

```bash
# Install package
pip3 install pretty-tables

# Install locally
make install

# Get Makefile help
make help
```

## Usage

Pretty Tables is simple to use. Pass the `generate_table` function an array of headers and a 2 dimensional array of rows (each row must match the length of the headers) and generate a table! Pass an optional `empty_cell_placeholder` to change the default behavior or what `None` will say in the table.

Pretty Tables will automatically validate the input and convert each item to a string before returning successfully; however, you can pass Pretty Tables any data type within an array. In the following example, we are using integers, booleans, None, and strings:

```python
from pretty_tables import PrettyTables


headers = ['ID', 'Name', 'Occupation', 'Employed']
rows = [
    [1, 'Justin', 'Software Engineer', True],
    [2, 'Misty', 'Receptionist', False],
    [3, 'John', None, False],
]

table = PrettyTables.generate_table(
    headers=headers, 
    rows=rows, 
    empty_cell_placeholder='No data'
)
print(table)
```

## Development

```bash
# Lint the project
make lint

# Run tests
make test

# Run test coverage
make coverage
```

## Attribution

- [Stack Overflow question on formatting tables for console](https://stackoverflow.com/a/8356620/865091)
- Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon"> www.flaticon.com</a>
