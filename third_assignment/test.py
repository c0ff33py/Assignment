# Personal Expense Tracker using OOP and MongoDB
# This is a simple console app for tracking expenses.
# It uses classes (OOP) and saves data in MongoDB (a database).
# For beginners: We have two classes - one for a single expense, one for managing all expenses.
# You need to install PyMongo: pip install pymongo
# And have MongoDB running (local on port 27017 by default).
# Updated: Now loops for valid inputs instead of aborting on errors.

import datetime  # Helps with dates
from pymongo import MongoClient  # Connects to MongoDB
from pymongo.errors import ConnectionFailure  # For error handling


class Expense:
    """
    This class is like a blueprint for one expense.
    It holds the details: what it was, how much, when.
    """
    def __init__(self, description, amount, date):
        # Save the details
        self.description = description  # What was the expense for? (text)
        self.amount = amount  # How much money? (number)
        self.date = date  # When did it happen? (text like '2025-10-02')

    def to_dict(self):
        """
        Turns this expense into a simple dictionary (key-value pairs).
        MongoDB likes dictionaries to save data.
        """
        return {
            'description': self.description,
            'amount': self.amount,
            'date': self.date
        }

    def __str__(self):
        """
        How to print this expense nicely.
        """
        return f"Description: {self.description}, Amount: {self.amount}, Date: {self.date}"


class ExpenseTracker:
    """
    This class manages all expenses. It talks to MongoDB to save/load data.
    Like a manager that keeps track of everything.
    """
    def __init__(self):
        # Connect to MongoDB (local by default)
        self.client = MongoClient('mongodb://localhost:27017/')  # Where MongoDB is
        self.db = self.client['expense_db']  # Our database name
        self.collection = self.db['expenses']  # Table-like collection for expenses

        # Test if connected
        try:
            self.client.admin.command('ismaster')  # Simple check
            print("Connected to MongoDB! Ready to track expenses.")
        except ConnectionFailure:
            print("Cannot connect to MongoDB. Make sure it's running.")
            exit()  # Stop if no connection

    def get_valid_description(self):
        """
        Keep asking until user enters a non-empty description.
        """
        while True:
            description = input("What was the expense for? ").strip()  # Remove extra spaces
            if description:  # If not empty
                return description
            print("Description can't be empty. Please try again.")

    def get_valid_amount(self):
        """
        Keep asking until user enters a positive number for amount.
        """
        while True:
            try:
                amount_str = input("How much was it? (number) ").strip()
                amount = float(amount_str)
                if amount > 0:
                    return amount
                else:
                    print("Amount must be positive. Please try again.")
            except ValueError:  # If not a number
                print("Please enter a valid number for amount. Try again.")

    def get_valid_date(self):
        """
        Keep asking until user enters a valid date or uses today.
        """
        while True:
            date_input = input("Date (YYYY-MM-DD) or Enter for today: ").strip()
            if not date_input:
                return datetime.date.today().strftime("%Y-%m-%d")  # Today's date

            try:
                # Check if date is correct format
                datetime.datetime.strptime(date_input, "%Y-%m-%d")
                return date_input
            except ValueError:
                print("Bad date format (use YYYY-MM-DD). Please try again or press Enter for today.")

    def add_expense(self):
        """
        Ask user for details (with validation loops), make an Expense, save to MongoDB.
        """
        # Get valid inputs using helper methods
        description = self.get_valid_description()
        amount = self.get_valid_amount()
        date = self.get_valid_date()

        # Create expense object
        new_expense = Expense(description, amount, date)

        # Save to MongoDB
        result = self.collection.insert_one(new_expense.to_dict())
        print(f"Added! MongoDB ID: {result.inserted_id}")

    def view_all_expenses(self):
        """
        Get all expenses from MongoDB and print them.
        """
        # Fetch all from database
        all_expenses = list(self.collection.find())  # Get as list

        if not all_expenses:
            print("No expenses yet. Add some!")
            return

        print("\nYour Expenses:")
        for exp in all_expenses:
            # Print ID and details
            print(f"ID: {exp['_id']}, {Expense(exp['description'], exp['amount'], exp['date'])}")

    def view_total_expenses(self):
        """
        Add up all amounts from MongoDB.
        Simple way: loop and sum.
        """
        all_expenses = list(self.collection.find())
        if not all_expenses:
            print("Total: 0.00")
            return

        total = 0
        for exp in all_expenses:
            total += exp['amount']  # Add each amount

        print(f"Total spent: {total:.2f}")  # Show with 2 decimals

    def delete_expense(self):
        """
        Ask for ID, remove from MongoDB if found.
        """
        all_expenses = list(self.collection.find())
        if not all_expenses:
            print("Nothing to delete.")
            return

        # Show current IDs
        print("Current IDs:")
        for exp in all_expenses:
            print(f" - {exp['_id']}")

        id_to_delete = input("Enter ID to delete: ").strip()
        if not id_to_delete:
            print("No ID entered.")
            return

        from bson import ObjectId  # For MongoDB IDs
        try:
            # Turn string ID to MongoDB ObjectId
            obj_id = ObjectId(id_to_delete)
        except:
            print("Bad ID format. Must be a valid MongoDB ID.")
            return

        # Delete it
        result = self.collection.delete_one({'_id': obj_id})
        if result.deleted_count > 0:
            print("Deleted successfully!")
        else:
            print("ID not found.")

    def close(self):
        """
        Close connection when done.
        """
        self.client.close()


def main():
    """
    The menu loop. Runs the app.
    """
    tracker = ExpenseTracker()  # Start the manager

    while True:  # Keep running until exit
        print("\n" + "=" * 40)
        print("Personal Expense Tracker with MongoDB")
        print("=" * 40)
        print("[1] Add New Expense")
        print("[2] View All Expenses")
        print("[3] View Total Expenses")
        print("[4] Delete Expense")
        print("[5] Exit")
        print("=" * 40)

        choice = input("Enter your choice(1-5): ").strip()

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_all_expenses()
        elif choice == '3':
            tracker.view_total_expenses()
        elif choice == '4':
            tracker.delete_expense()
        elif choice == '5':
            print("Goodbye! Thanks for using the tracker.")
            break
        else:
            print("Please choose 1-5.")

    tracker.close()  # Clean up


# Start the app
if __name__ == "__main__":
    main()