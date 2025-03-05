
class Remove_Book:
    def __init__(self,book_data):
        self.book_data = book_data
    def remove_book(self):
        if not self.book_data.book_list:
            print("No books available.")
            return

        book_id = input("Please enter the book id to remove: ")
        updated_books = []
        for i in self.book_data.book_list:
            if i['book_id'] != book_id:
                updated_books.append(i)
        
        if len(updated_books) == len(self.book_data.book_list):
            print(f"No book found with ID: {book_id}.")
        else:
            self.book_data.save_book(updated_books)
            self.book_data.book_list = updated_books
            print('Book deleted successfully.')