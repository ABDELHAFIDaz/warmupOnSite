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
    
# Bloc 2 ===============================================================

class BankAccount:
    
    bank_accounts = 0
    
    def __init__(self, balance):
        self.__balance = balance
        BankAccount.bank_accounts += 1
        
    @property
    def balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if 0 < amount:
            self.__balance += amount
        
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            
    @classmethod
    def num_of_accounts(cls):
        return cls.bank_accounts
    
    @staticmethod
    def convert_currency(amount, rate):
        if rate > 0:
            return amount * rate

# Bloc 3 ===============================================================

from abc import ABC, abstractclassmethod

class Vehicule(ABC):
    def __init__(self, brand, registration):
        self.brand = brand
        self.__registration = registration
    
    @abstractclassmethod  
    def tarif_journalier(self):
        pass
    
    def __str__(self):
        return f'{self.__class__.__name__} -- {self.brand} -- {self.__registration}'
    
    
class Car(Vehicule):
    def __init__(self, brand, registration, num_seats, base=20):
        super().__init__(brand, registration)
        self.num_seats = num_seats
        self.__tarif = base + num_seats
    
    def tarif_journalier(self):
        return self.__tarif

    def __str__(self):
        return super().__str__() + f' -- {self.num_seats} seats -- {self.__tarif}/day'
    
    
    
class Bike(Vehicule):
    def __init__(self, brand, registration, cylindree, base=10):
        super().__init__(brand, registration)
        self.cylindree = cylindree
        self.__tarif = base + cylindree

    def tarif_journalier(self):
        return self.__tarif

    def __str__(self):
        return super().__str__() + f' -- {self.cylindree} cylindree -- {self.__tarif}/day'


class truck(Vehicule):
    def __init__(self, brand, registration, charge_utile, base=40):
        super().__init__(brand, registration)
        self.charge_utile = charge_utile
        self.__tarif = base + self.charge_utile
        
    def tarif_journalier(self):
        return self.__tarif

    def __str__(self):
        return super().__str__() + f' -- {self.charge_utile} charge_utile -- {self.__tarif}/day'
    

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
    
    # bloc 2:
    
    # acc = BankAccount(500)
    # # BankAccount.bank_accounts = 0 # this will change it for all the instances since we've used the class name to call the property
    # acc.deposit(100)
    # print(acc.balance)
    # acc.withdraw(50)
    # print(acc.balance)
    # print(acc.bank_accounts)
    # print(acc.num_of_accounts())
    
    # bloc 3:
    
    # garage = [
    #     Car('audi', 32323, 5),
    #     Bike('bmw', 123321, 8),
    #     truck('renault', 112233, 100)
    # ]
        
    # for vehicule in garage:
    #     print(vehicule.brand, "->", vehicule.tarif_journalier())
    
    # for vehicule in garage:
    #     print(vehicule)
        
        
        
    
if __name__ == '__main__':
    main()