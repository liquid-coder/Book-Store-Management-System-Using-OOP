
class View_Book():
    def __init__(self,book_data):
        self.book_data = book_data
    def view_books(self):
        if not self.book_data.book_list:
            print("No books available.")
            return

        print("\n--- List of Books ---")
        for i in self.book_data.book_list:
            print(f"Title: {i['title']}\nAuthor: {i['author']}\nBook ID: {i['book_id']}\nGenre: {i['genre']}\nPrice: {i['price']} Tk\nStock: {i['stock']}")
            print('------')
