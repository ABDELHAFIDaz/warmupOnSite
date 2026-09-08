# Bloc 1 ===============================================================


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            return self.title
    
    def rendre(self):
        if not self.available:
            self.available = True
            
    
    def __str__(self):
        return f'"{self.title}" by {self.author} -- {'Available' if self.available else 'Not available'}'


  
class Member:
    def __init__(self, name, borrowed_books = []):
        self.name = name
        self.borrowed_books = borrowed_books
        
    def borrow_book(self, book):
        if b := book.borrow():
            self.borrowed_books.append(b)
            print(f'{self.name} has borrowed ({b}) book')
        else:
            print(f'[ERROR] : The book "{book.title}" is unavailable')
    
    def return_book(self, book):
        if book.title in self.borrowed_books:
            self.borrowed_books.remove(book.title)
            book.rendre()
    
    def borrowed_books_stats(self):
        return len(self.borrowed_books)
        


def main():
    # bloc 1:
    
    # english_book = Book('english in 5min', 'someone')
    # spanish_book = Book('spanish in 5 min', 'someone')

    # member1 = Member('hafid')
    # cdm = Member('cdm')
    
    # member1.borrow_book(english_book)
    # member1.borrow_book(spanish_book)
    # cdm.borrow_book(english_book)
    
    # print(member1.borrowed_books)
    # print(english_book)
    
    # member1.return_book(english_book)
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()