
class Add_book():
    def __init__(self,book_data):
        self.book_data = book_data
    def add_book(self):    
        print("\n--- Add a New Book ---")
        try:
            
            title = input("Enter the book title: ")
            
            if  title.isdigit():
              print('Title needs to be a string') 
              return
            author = input("Enter the author: ")
            book_id = input("Enter the book id: ")
            for i in self.book_data.book_list:
                if i['book_id'] == book_id:
                    print('Same id is assigned to another book')
                    return
            genre = input("Enter the genre: ")
            price = float(input("Enter the price: "))
            if price < 0:
                print("Error: Price cannot be negative.")
                return
            stock = int(input("Enter the quantity in stock: "))
            if stock < 0:
                print("Error: Quantity cannot be negative.")
                return





    
            new_book = {
                "title": title,
                "author": author,
                "book_id": book_id,
                "genre": genre,
                "price": price,
                "stock": stock
            }
            self.book_data.book_list.append(new_book)
            self.book_data.save_book(self.book_data.book_list)        
            print('Book added successfully')
            
        
        except ValueError:
            print("Invalid choice. Please enter valid choice.")
        
