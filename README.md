# TM: Today's Mathematics (Stoic Mod-5 System)

Static site that displays daily Stoic virtues using a mod-5 system connected to a SQLite3 database.

## Prerequisites

- Python 3.8+
- [uv](https://pypi.org/project/uv/) (project manager)

## Setup

```bash
# Install dependencies
python3 -m pip install --upgrade pip
pip install uv
uv sync

# Initialize database
uv run python3  data/init_db.py

# Run the app locally
uv run python3 -m main.py
```
