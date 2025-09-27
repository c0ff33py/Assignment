# Mini Bank
class Bank:
    def __init__(self):
        self.accounts = {}
    # Register Method
    def register(self):
        username = input("Please enter username: ")

        if username in self.accounts:
            print("Username already exist!")
            return
        
        password = input("Please enter password: ")
        re_password =input("Please re-enter password: ")
        if re_password != password:
            print("password does not match!")
            return
        self.accounts[username] = {"password": password, "balance": 0.0}
        print("Register successful!")

    # Login Method
    def login(self):
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")

        acc = self.accounts.get(username)
        if acc and acc["password"] == password:
            print(f"Welcome {username}")
            self.account_menu(username)
        else:
            print("Invalid username or password")
    
    # account_menu
    def account_menu(self,username):
        while True:
            acc = self.accounts[username]
            print(f"\n[User: {username}] Balance: {acc["balance"]:.2f}")
            print("[1] Deposit")
            print("[2] Withdraw")
            print("[3] Check_balance")
            print("[4] Transfer")
            print("[0] Logout")
            choice = input("Choose option: ")

            if choice == "1":
                self.deposit(username)
            elif choice == "2":
                self.withdraw(username)
            elif choice == "3":
                self.check_balance(username)
            elif choice == "4":
                self.transfer(username)
            elif choice == "0":
                self.logout(username)
                break
            else:
                print("Invalid option")

    def deposit(self,username):
        amount = float(input("enter deposit: "))
        self.accounts[username]["balance"] += amount
        print("Deposit successful")
    
    # withdraw method
    def withdraw(self, username):
        try:
            amount = float(input("Withdraw amount: "))
        except ValueError:
            print("Please enter a number.")
            return

        if amount <= 0:
            print("Amount must be greather than 0.")
            return
        
        if self.accounts[username]["balance"] >= amount:
            self.accounts[username]["balance"] -= amount
            print("Withdraw successful.")

        else:
            print("Not enough balance.")
            

    # money transfer method
    def transfer(self, sender):
        to_user = input("Enter (username) who you want to send money: ")
        amount = float(input("Enter amount: "))
    
        if to_user not in self.accounts:
            print("Reciver not found.")
            return
        
        if self.accounts[sender]["balance"] >= amount:
            self.accounts[sender]["balance"] -= amount
            self.accounts[to_user]["balance"] += amount
            print("Transfer successful.")
        else:
            print("Not enough balance.")
            
    # check balance method
    def check_balance(self, username):
        balance = self.accounts[username].get("balance", 0)
        print(f"Your balance is: {balance}")

    # logout method
    def logout(self, username=None): # after logout , not used user
        if username:
            print(f"Goodbye, {username}")
        else:
            print("Goodbye")
    

def main():
    bank = Bank()
    while True:
        print("\n=====Mini Bank======")
        print("[1] * Register")
        print("[2] * Login")
        print("[0] * Exit")
        choice = input("Please choose options: ")

        if choice == "1":
            bank.register()
        elif choice == "2":
            bank.login()
        elif choice == "0":
            bank.logout()
            break
        else:
            print("Invalid options")
            
        
        
if __name__ == "__main__":
    main()
