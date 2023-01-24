# catg
## Overview
This library is to generate necessary files with some template code when user makes new use case on clean architecture.  

## How to setup
```python
pip install -e .
```

## How to use
```bash
catg generate_template domain
```
By this the basic template will be made.  
```
.
└── domain
    ├── adapter
    │   └── __init__.py
    ├── dto
    │   └── __init__.py
    └── use_case
        └── __init__.py

```
Whenever you need to add new use case, the command below will generate the necessary files with some template code.  
```
cd domain
catg add_use_case get_report
```
Each directories have new file for the new use case, this time, get_report.
```
.
├── adapter
│   ├── get_report.py
│   └── __init__.py
├── dto
│   ├── get_report.py
│   └── __init__.py
└── use_case
    ├── get_report.py
    └── __init__.py
```