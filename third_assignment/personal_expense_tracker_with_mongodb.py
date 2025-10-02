# Personal Expense Tracker using OOP and MongoDB

import datetime
from pymongo import MongoClient # that for connect to MongoDB
from pymongo.errors import ConnectionFailure # for error hanling

class Expense:
    def __init__(self, description, amount, date):
        """ Save the details"""
        self.description = description
        self.amount = amount
        self.date = date

    def to_dict(self):
        return {
            "description": self.description,
            "amount": self.amount,
            "date": self.date
        }

    def __str__(self):
        """That is how to print expense"""
        return f"Description: {self.description}, Amount: {self.amount}, Date: {self.date}"

class ExpenseTracker:
    """This class to manage all expenses and save/ load data"""
    def __init__(self):
        """# Connect to MongoDB"""
        self.client = MongoClient('mongodb://localhost:27017/') # run in localhost
        self.db = self.client['expense_db'] # database name
        self.collection = self.db['expenses'] # table name
        # Test for connection
        try:
            self.client.admin.command('ismaster')
            print("Connected to MongoDB!. Ready to rack expenses.")
        except ConnectionFailure:
            print("Cannot connect to MongoDB.")
            exit() # Stop if not connection

    def get_valid_description(self):
        while True:
            description = input("What was the expense for?").strip()
            if description:
                return description
            print("Description can't be empty. Please try again.")
    
    def get_valid_amount(self):
        while True:
            try:
                amount_str = float(input("How much was it?(number)"))
                amount = float(amount_str)
                if amount > 0:
                    return amount
                else:
                    print("Amount must be positive number.")
            except ValueError:
                print("Please enter a valid number")
    
    def get_valid_date(self):
        while True:
            date_input = input("Date (YYYY-MM-DD) or Enter for today: ").strip()
            if not date_input:
                return datetime.date.today().strftime("%Y-%m-%d") 
            try:
                datetime.datetime.strptime(date_input, "%Y-%m-%d")
                return date_input
            except ValueError:
                print("Please enter correct date format('YYYY-MM-DD') or Enter for today.")
    
    def add_expense(self): #Ask user for details
        description = self.get_valid_description()
        amount = self.get_valid_amount()
        date = self.get_valid_date()

        # Create expense object
        new_expense = Expense(description, amount, date)

        # Save to MongoDB
        result = self.collection.insert_one(new_expense.to_dict())
        print(f"Added! MongoDB ID: {result.inserted_id}")
                
    def view_all_expenses(self):
        """Get all expenses from MongoDB and Print them"""
        # fetch all data from database
        all_expenses = list(self.collection.find()) # Get as list

        if not all_expenses:
            print("No expenses found. Add something")
            return

        print("\nYour Expenses:")
        for exp in all_expenses:
            # print ID and detail
            print(f"ID: {exp['_id']},Description: {Expense(exp['description'],exp['amount'], exp['date'])}")

    def view_total_expenses(self):
        all_expenses = list(self.collection.find())
        if not all_expenses:
            print("Total: 0.00")
            return

        total = 0
        for exp in all_expenses:
            total += exp['amount']
        print(f"Total spent: {total:.2f}")

    def delete_expense(self):
        """Ask ID to delete"""
        all_expenses = list(self.collection.find())
        if not all_expenses:
            print("Noting to delete.")
            return

        #Show current IDs
        print("Current IDs:")
        for exp in all_expenses:
            print(f" - {exp['_id']}")

        id_to_delete = input("Please enter ID to delete: ").strip()
        if not id_to_delete:
            print("No ID entered.")
            return
        from bson import ObjectId # For MongoDB IDs
        try:
            # Turn string ID to MongoDB Object
            obj_id = ObjectId(id_to_delete)
        except:
            print("ID not found.")
            return

        #Delete it
        result = self.collection.delete_one({'_id': obj_id})
        if result.deleted_count > 0:
            print("Deleted successfully.")
        else:
            print("ID not found.")

    def close(self):
    # close the connection
        self.client.close()

def main():
    # menu
    tracker = ExpenseTracker()
    while True:
        print("\n" + "=" * 30)
        print("Personal Expense Tracker with MongoDB")
        print("=" * 30)
        print("[1] Add New Expense")
        print("[2] View All Expenses")
        print("[3] View Total Expenses")
        print("[4] Delete Expense")
        print("[5] Exit")
        print("=" * 30)

        choice = input("Enter your choice(1-5): ").strip()
        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_all_expenses()
        elif choice == "3":
            tracker.view_total_expenses()
        elif choice == "4":
            tracker.delete_expense()
        elif choice == "5":
            print("Exiting.. Goodbye!")
            break
        else:
            print("Invalid choice.")
            
    tracker.close()

if __name__ == "__main__":
    main()

