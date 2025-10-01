# Personal Expense Tracker

import datetime

class Expense:
    def __init__(self, description, amount, date):
        self.id = id(self)
        self.description = description
        self.amount = amount
        self.date = date

    def __str__(self):
        return f"ID: {self.id}, Description: {self.description}, Amount: {self.amount}, Date: {self.date}"
    

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self):
        description = input("Enter description: ").strip()
        if not description:
            print("Descripiton cannot be empty. Aborting.")
            return
        
        try:
            amount = float(input("Enter amount: "))
            if amount < 0:
                print("Amount cannot be negative. Aborting.")
                return
        except ValueError:
            print("Invalid amount. Aborting.")
            return
        
        date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_input:
            try:
                datetime.datetime.strptime(date_input, "%Y-%m-%d")
                date = date_input
            except ValueError:
                print("Invalid date format. Using today's date.")
                date = datetime.date.today().strftime("%Y-%m-%d")
                
        else:
            date = datetime.date.today().strftime("%Y-%m-%d")
        
        # Create and add the expense

        expense = Expense(description, amount, date)
        self.expenses.append(expense)
        print(f"Expense added with ID: {expense.id}")

    def view_all_expenses(self):
        if not self.expenses:
            print("No expesnes recorded yet.")
            return
        
        print("\All Expenses:")
        for expense in self.expenses:
            print(str(expense))

    def view_total_expense(self):
        total = sum(expense.amount for expense in self.expenses)
        print(f"Total Expenses: {total:.2f}")
    
    def delete_expense(self):
        if not self.expenses:
            print("No expenses to delete")
            return
        try:
            expense_id = int(input("Enter ID to Delete: "))
        except ValueError:
            print("Invalid ID.")
            return
        
        for i, expense in enumerate(self.expenses):
            if expense.id == expense_id:
                deleted = self.expenses.pop(i)
                print(f"Deleted expense: {deleted.description} (ID: {expense_id})")
                return
                
        print("Expense ID not found.")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n" + "=" * 30)
        print("Personal Expense Tracker")
        print("=" * 30)
        print("[1] Add New Expense")
        print("[2] View All Expense")
        print("[3] View Total Expense")
        print("[4] Delete an Expense")
        print("[5] Exit")
        print("=" * 30)

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 5.")
            continue

        if choice == 1:
            tracker.add_expense()
        elif choice == 2:
            tracker.view_all_expenses()
        elif choice == 3:
            tracker.view_total_expense()
        elif choice == 4:
            tracker.delete_expense()
        elif choice == 5:
            print("Goodbye!")
            break
        else:
            print("Invalid Choice. Please enter a number between 1 and 5")

if __name__ == "__main__":
    main()
            