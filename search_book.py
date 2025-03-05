
class Search_Book():        
    def __init__(self,book_data):
        self.book_data = book_data
        
    def search_book(self):
           
        while True:
            print("\n--- Search for a Book ---")
            print('Search Types -->')
            print('1. Book ID')
            print('2. Author')
            print('3. Genre')
            print('4. Exit')
            
            try:
                user_inp = int(input('Press : '))
            except ValueError:
                print('Please enter valid input !!!')
                continue  

            if user_inp == 1:
                id = input('Please enter book_id : ')
                found = False
                for i in self.book_data.book_list:
                    if i['book_id'] == id:
                        print('------')
                        print(f"Title: {i['title']}\nAuthor: {i['author']}\nGenre: {i['genre']}\nPrice: {i['price']} Tk\nStock: {i['stock']}")
                        print('------')
                        found = True
                        break
                if not found:
                    print('No such id is associated with any book !!!')

            elif user_inp == 2:
                writer = input('Please enter author name : ')
                found = False
                for i in self.book_data.book_list:
                    if i['author'].lower() == writer.lower():
                        print('------')
                        print(f"Title: {i['title']}\nAuthor: {i['author']}\nGenre: {i['genre']}\nPrice: {i['price']} Tk\nStock: {i['stock']}")
                        print('------')
                        found = True
                        break
                if not found:
                    print('No such author found !!!')

            elif user_inp == 3:
                genre = input('Please enter genre : ')
                found = False
                for i in self.book_data.book_list:
                    if i['genre'].lower() == genre.lower():
                        print('------')
                        print(f"Title: {i['title']}\nAuthor: {i['author']}\nGenre: {i['genre']}\nPrice: {i['price']} Tk\nStock: {i['stock']}")
                        print('------')
                        found = True
                        break
                if not found:
                    print('No such genre found !!!')

            elif user_inp == 4:
                break  

            else:
                print('Please enter from the given choices !!!')

