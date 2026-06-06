# RRAA Finance - Professional Finance Collection Management System

A professional offline finance collection management system built with Python, CustomTkinter, SQLite, and Plotly.

## Features

- Loan Management (VARAVU - Issue New Loan)
- Collection Management (ADAPPU - Collect Loan Repayment)
- Fixed 25% Interest Rate Calculation
- 10-Week Repayment Schedule
- Professional Dashboard with 3D Visualizations
- Comprehensive Reporting (PDF, Excel, CSV)
- Customer & Loan Ledgers
- Penalty Management
- Audit Logging
- Role-Based Access Control
- Receipt Generation

## Requirements

- Python 3.8+
- Windows 10/11
- SQLite3

## Installation

1. Clone or extract the project
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Database

The application uses SQLite with the following tables:
- customers
- loans
- collections
- penalties
- users
- audit_logs
- settings

Database is automatically initialized on first run.

## Architecture

- MVC Pattern
- Service Layer for Business Logic
- Database Abstraction Layer
- Type Hints Throughout
- Comprehensive Error Handling
- Logging System

## License

Proprietary