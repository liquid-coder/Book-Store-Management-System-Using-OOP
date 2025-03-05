import json
import os

class Book_Data:
    def __init__(self,file = 'books.json'):
        self.file = file 
        self.book_list = self.load_book()
    def load_book(self):
        if os.path.exists(self.file):
            if os.path.getsize(self.file)!=0:
                with open(self.file, "r") as f:
                    return json.load(f)
            else:
                return []
        else:
            return []

    def save_book(self,books):
        with open(self.file, "w") as f:
            json.dump(books, f, indent=4)