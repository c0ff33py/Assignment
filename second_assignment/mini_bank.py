# Mini Bank Cli application with file Handling

class Bank:
    def __init__(self):
        self.accounts_file = "accounts.txt"
        self.accounts = self.load_accounts()
        
    # File Handling
    def load_accounts(self):
        accounts = {}
        try:
            with open(self.accounts_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        username, password, balance = line.split(",")
                        accounts[username] = {"password": password, "balance": float(balance)}
        except FileNotFoundError:
            pass
        return accounts

        
    # save accounts method with file handling   
    def save_accounts(self):
        with open(self.accounts_file, "w", encoding="utf-8") as f:
            for username, acc in self.accounts.items():
                f.write(f"{username}, {acc['password']},{acc['balance']}\n")

    # Register method
    def register(self):
        username = input("Please enter username: ")

        if username in self.accounts:
            print("Username already exist.")
            return
        
        password = input("Please enter password: ")
        re_password = input("Please re-enter password: ")
        if re_password != password:
            print("Password does not match!")
            return
        
        self.accounts[username] = {"password":password, "balance": 0.0}
        self.save_accounts()
        print("Register successful.")

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
    
    # account_menu method
    def account_menu(self, username):
        while True:
            acc = self.accounts[username]
            print(f"\n[User: {username}] Balance: {acc['balance']:.2f}")
            print("[1] Deposit")
            print("[2] Withdraw")
            print("[3] Check_balance")
            print("[4] Transfer")
            print("[0] Logout")

            choice = input("Choose opton: ")
            if choice == '1':
                self.deposit(username)
            elif choice == '2':
                self.withdraw(username)
            elif choice =='3':
                self.check_balance(username)
            elif choice == '4':
                self.transfer(username)
            elif choice == '0':
                self.logout(username)
                break
            else:
                print("Invalid option.")

    # Deposit method           
    def deposit(self, username):
        try:
            amount = float(input("Enter deposit amount: "))
        except ValueError:
            print("Please enter a number.")
            return
        
        if amount <= 0: # check zero or less than 0
            print("Amount must be greater than '0'.")
            return
        
        self.accounts[username]["balance"] += amount
        self.save_accounts()
        print("Deposit successful.")

    # withdraw method
    def withdraw(self, username):
        try:
            amount = float(input("Pls withdraw amount: "))
        except ValueError:
            print("Amount must be number")
            return
        
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
            
        if self.accounts[username]["balance"] >= amount:
            self.accounts[username]["balance"] -= amount
            self.save_accounts()
            print("Withdraw successful.")
        else:
            print("Not enough balance!")
            
    # Transfer method  
    def transfer(self, sender):
        to_user = input("Enter [username] who you want to send money: ")
        try:
            amount = float(input("Enter amount to send: "))
        except ValueError:
            print("Please enter a number.")
            return
        
        if to_user not in self.accounts:
            print("Reciver not found.")
            return
        
        if self.accounts[sender]["balance"] >= amount:
            self.accounts[sender]["balance"] -= amount
            self.accounts[to_user]["balance"] += amount
            self.save_accounts()
            print("Transfer successfully.")
        else:
            print("Not enough balance.")

    # check balance method
    def check_balance(self, username):
        balance = self.accounts[username].get("balance", 0)
        print(f"Your balance is : {balance:.2f}")

    # Logout method
    def logout(self, username= None):
        if username:
            print(f"GooooooodByeeeee {username}")
        else:
            print("Goodbye!")

def main():
    bank = Bank()
    while True:
        print("\n======Mini Bank Cli Application======")
        print("[1] * Register")
        print("[2] * Login")
        print("[0] * Exit")
        
        choice = input("Please choose option: ")
        if choice == "1":
            bank.register()
        elif choice == "2":
            bank.login()
        elif choice =="0":
            bank.logout()
            break
        else:
            print("Invalid options")

if __name__ == "__main__":
    main()
            
    
        
                
        
            
        
                    
            

            
            
            
                            
            
            
            
            
            