class Library:
    book_list = []
    def __init__(self):
        pass
    def entry_book(self, book):
        Library.book_list.append(book)
class Book(Library): 
    def __init__(self, book_id, title, author, availability=True):
        super().__init__()
        self.__book_id = book_id
        self._title = title
        self._author = author
        self._availability = availability
        self.entry_book(self)  
    def get_book_id(self):
        return self.__book_id
    def set_book_id(self, new_book_id):
        self.__book_id = new_book_id
    def borrow_book(self):
        if self._availability:
            self._availability = False
            print(f"You've successfully borrowed {self._title}. Please return it within 10 days. Thank you.")
        else:
            print(f"{self._title} is already borrowed.")
    def return_book(self):
        if not self._availability:
            self._availability = True
            print(f"Thank you for returning {self._title}.")
        else:
            print(f"{self._title} was not borrowed.")

    def view_book_info(self):
        if self._availability:
            availability_status="Available" 
        else:
            availability_status="Unavailable"
        print(f"ID: {self.get_book_id()} ,Title: {self._title} ,Author: {self._author} ,Availability: {availability_status}")


def menu():
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        cho = input("Enter your choice: ")
        if cho == "1":
            if not Library.book_list:
                print("No books are currently available in the library.")
            else:
                print("\nAvailable Books:")
                for book in Library.book_list:
                    book.view_book_info()
        elif cho == "2":
            book_id = int(input("Enter the book ID to borrow: "))
            for book in Library.book_list:
                if book.get_book_id() == book_id:
                    book.borrow_book()
                    break
            else:
                print("Invalid book ID! Try again.")
        elif cho == "3":
            book_id = int(input("Enter the book ID to return: "))
            for book in Library.book_list:
                if book.get_book_id() == book_id:  
                    book.return_book()
                    break
            else:
                print("Error: Invalid book ID!")
        elif cho == "4":
            print("Goodbye, my dear reader!")
            break
        else:
            print("Invalid choice! Try again.")
book1 = Book(1, "Python", "Don")
book2 = Book(2, "Data Science", "Abdullah")
menu()
