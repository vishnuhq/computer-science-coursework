# CS 555: Agile Methods for Software Development

Coursework from CS 555 at Stevens Institute of Technology, Spring 2025.

## Assignments

### Test-First Assignment

A currency converter implemented using test-driven development. Demonstrates writing tests before implementation code.

**Files:**
- `currency_converter.py` - Currency conversion logic with exchange rate management
- `test_currency_converter.py` - Unit tests for the converter

### Practice Refactoring Assignment

A savings goal tracker with currency conversion support. The code was refactored for improved quality while maintaining test coverage.

**Files:**
- `savings_goal_tracker.py` - Savings tracking and goal management
- `currency_converter.py` - Supporting currency conversion module
- `test_savings_goal_tracker.py` - Unit tests

## Running Tests

```bash
cd test-first-assignment
python -m pytest test_currency_converter.py

cd ../practice-refactoring-assignment
python -m pytest test_savings_goal_tracker.py
```

## Requirements

- Python 3.8+
- pytest
