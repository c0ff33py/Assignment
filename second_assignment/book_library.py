# Book library Project with file handling

class BookLibrary:
    def __init__(self):
        self.books_file = "books.txt"
        self.rented_file = "rented.txt"
        self.books = self.load_books() # dictionary: title -> author
        self.rented_books = self.load_rented() # dictionary: title -> renter

    # File Handling
    def load_books(self):
        books = {}
        try:
            with open(self.books_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line: # skip empty lines
                        title, author = line.split(",")
                        books[title] = author # key = title, value = author
        except FileNotFoundError:
            pass 
        return books
    
    #method save_books
    def save_books(self):
        with open(self.books_file, "w", encoding="utf-8") as f:
            for title, author in self.books.items():
                f.write(f"{title}, {author}\n")

    def load_rented(self):
        rented = {}
        try:
            with open(self.rented_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        title, renter = line.split(",")
                        rented[title] = renter
        except FileNotFoundError:
            pass
        return rented
    
    def save_rented(self):
        with open(self.rented_file, "w", encoding="utf-8") as f:
            for title, renter in self.rented_books.items():
                f.write(f"{title},{renter}\n")

    # making features
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")

        if title in self.books:
            print("This book already exists.")
        else:
            self.books[title] = author
            self.save_books()
            print(f"Book '{title}' added.")

    def view_books(self):
        if not self.books:
            print("No books in the library yet.")
            return
        
        print("\n-----Library Books-----")
        for title, author in self.books.items():
            if title in self.rented_books:
                status = f"Rented by {self.rented_books[title]}"
            else:
                status = "Available"
            print(f"Title : {title} | Author: {author} | Status: {status}")
        print('-----------------------------\n')

    def rent_book(self):
        title = input("Enter book title to rent: ")

        if title not in self.books:
            print("book not found")
            return
        
        if title in self.rented_books:
            print(f"Sorry, '{title}' already rented by {self.rented_books[title]}")
        else:
            renter = input("Enter your name: ")
            self.rented_books[title] = renter
            self.save_rented()
            print(f"You rented '{title}', Enjoy reading.")

    def return_book(self):
            title = input("Enter book title to return: ")

            if title in self.rented_books:
                self.rented_books.pop(title)
                self.save_rented()
                print(f"'{title}' returned. Thanks!")
            else:
                print("That book is not rented.")

    def menu(self):
        while True:
            print("\n--- Book Library Menu ---")
            print("[1] Add Book")
            print("[2] View Books")
            print("[3] Rent Book")
            print("[4] Return Book")
            print("[5] Exit")

            choice = input("Choose (1-5): ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.rent_book()
            elif choice == "4":
                self.return_book()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option. Try again.")

# Run the program
if __name__ == "__main__":
    library = BookLibrary()
    library.menu()
            
            
            
            
            
            
            