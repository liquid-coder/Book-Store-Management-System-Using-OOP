from add_book import Add_book
from view_books import View_Book
from search_book import Search_Book
from remove_book import Remove_Book
from book_data import Book_Data

def display_menu():

    print("\n--- Book Store Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

def main():

    book_data = Book_Data()

    books = book_data.load_book()


    if books:
        print('List of Books in our Library :-')
        for count, book in enumerate(books, start=1):
            print('---------- ')
            print('Book Number -', count)
            print(f"Title: {book['title']}\nAuthor: {book['author']}\nBook ID: {book['book_id']}\nGenre: {book['genre']}\nPrice: {book['price']} Tk\nStock: {book['stock']}")
            print('----------')
    else:
        print('Sorry, no books found in the library!')
        print('Please add books to the library -->')


    add_book = Add_book(book_data)
    view_books = View_Book(book_data)
    search_book = Search_Book(book_data)
    remove_book = Remove_Book(book_data)


    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book.add_book()
        elif choice == "2":
            view_books.view_books()
        elif choice == "3":
            search_book.search_book()
        elif choice == "4":
            remove_book.remove_book()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()