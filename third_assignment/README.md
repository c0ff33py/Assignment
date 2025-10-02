# Personal Expense Tracker (Python OOP + MongoDB)

A console-based expense tracker that stores records in **MongoDB**, written with **OOP** principles.

## Features

- Add a new expense (description, amount, date)
- View all expenses (shows MongoDB `_id`)
- View total expenses
- Delete an expense by `_id`
- Input validation:
  - Description must not be empty
  - Amount must be a positive number
  - Date must be `YYYY-MM-DD` (or press Enter for today)

## Tech

- Python 3.9+ (works on 3.8+ too)
- MongoDB (local or Atlas)
- PyMongo

## Setup

1. **Clone the project**
   ```bash
   git clone https://github.com/c0ff33py/Assignment.git
   cd third_assignment

2. **Create and activate a virtual environment**
python -m venv .venv
# macOS/Linux
source .venv/bin/activate
# Windows
.venv\Scripts\activate

3. install dependencies
pip install -r requirements.txt

4. make sure MongoDB is running
local: mongodb://localhost:27017

### Run
python personal_expense_tracker_with_mongodb.py

```### Menu like this
========================================
Personal Expense Tracker with MongoDB
========================================
[1] Add New Expense
[2] View All Expenses
[3] View Total Expenses
[4] Delete Expense
[5] Exit
========================================
Enter your choice (1-5):```
