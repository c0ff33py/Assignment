# Book Library project 

# Class
class BookLibrary:
    def __init__(self):
        self.books = {} # key=book title, value= author
    
        self.rented_books = {} # keep track of rented books separately
    # book add method
    def add_book(self):
        # Ask the user for book title and author
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")

        # Store inside dictionary
        if title in self.books:
            print("This book is already exists in the library!")
        else:
            self.books[title] = author
            print(f"Book '{title}' by {author} add successfully.")
    # view book method
    def view_book(self):

        # check if library is empty
        if not self.books:
            print("No books in the library yet.")
            return
        
        # Print all books in the library
        print("\n----- Library Books-------")
        for title, author in self.books.items():
            status = "Available"
            if title in self.rented_books:
                status = f"Rented by {self.rented_books[title]}"
            print(f"Title : {title}, Author {author}, Status: {status}")
        print("----------------------\n")

    # remove book method
    def rent_book(self):
        #Ask which book to rent
        title = input("Enter the book title you want to rent: ")

        # Check if book exists in library
        if title in self.books:
            # check again if already rented
            if title in self.rented_books:
                print(f"Sorry, '{title}' is already rented by {self.rented_books[title]}")
            else:
                renter = input("Enter your name: ")
                self.rented_books[title] = renter
                print(f"You have successfully rented '{title}. Enjoy reading!")
        else:
            print("Book not found in library.")
            
        
        #menu method
    def menu(self):
#Main menu loop
        while True:
            print("\n-----Book Library Menu-----")
            print("[1] Add Book")
            print("[2] View Books")
            print("[3] Rent Book")
            print("[4] Exit")
                
            choice = input("Choose an option (1-4): ")
            if choice == "1":
                self.add_book()
            elif choice =="2":
                self.view_book()
            elif choice == "3":
                self.rent_book()
            elif choice == "4":
                print("Exiting...Goodbye!")
                break
            else:
                print("Invalid choice, Please try again.")
                    
if __name__ == "__main__":
    library = BookLibrary()
    library.menu()                  

                
                
                
                
                
                