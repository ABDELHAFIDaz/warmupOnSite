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
    

# Bloc 4 ===============================================================

class Modele(ABC):
    @abstractclassmethod
    def entrainer(self, data):
        pass
    
    @abstractclassmethod
    def predire(self, entree):
        pass

from statistics import mean

class ModeleMoyenne(Modele):
    def entrainer(self, data):
        if data:
            self.moyenne = mean(data)
    
    def predire(self, entree):
        if self.moyenne:
            return self.moyenne
        return 0

class ModeleLineaireSimple(Modele):
    
    def __init__(self, poids, biais):
        self.poids = poids
        self.biais = biais
        
        
    def entrainer(self, data):
        if data:
            self.data = data
    
    def predire(self, entree):
        try:
            y = (self.poids * float(entree)) + self.biais
            return y 
        except (ValueError, TypeError):
            return 'ERROR: Invalid entree'
    

class Pipeline:
    
    def __init__(self, pretraitement, modele):
        self.pretraitement = pretraitement
        self.modele = modele
        
    def executer(self, data, entree):
        scaled_data = self.pretraitement(data)
        self.modele.entrainer(scaled_data)
        return self.modele.predire(entree)
    

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
        
    # bloc 4:
    
    # #md = Modele() # Error cuz we can't instantiate from an abstract class
    
    # data = [5, 8, 11]
    # modele = ModeleMoyenne()
    # modele.entrainer(data)
    # print(modele.predire(999))
    
    # modele = ModeleLineaireSimple(poids=2, biais=1)
    # modele.entrainer(data=None)
    # print(modele.predire(5))
    
    # mini challenge final:
        
    # def normaliser(data):
    #     maximum = max(data)
    #     return [d / maximum for d in data]
    
    # pipeline_moyenne = Pipeline(pretraitement=normaliser, modele=ModeleMoyenne())
    # pipeline_lineaire = Pipeline(pretraitement=normaliser, modele=
    # ModeleLineaireSimple(2, 1))
    
    # data = [5, 8, 11]
    
    # for pipeline in [pipeline_moyenne, pipeline_lineaire]:
    #     resultat = pipeline.executer(data, entree=5)
    #     print(type(pipeline.modele).__name__, "->", resultat)
    
    pass
    
    
if __name__ == '__main__':
    main()