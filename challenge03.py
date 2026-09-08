import json
# Bloc 1 ===============================================================================

def verify_age(age):
    try:
        age = int(age)
        if 0 <= age <= 120:
            return True
    except (ValueError, TypeError):
        print('Age must be a number\n')
        return False


def save_infos(infos):
    try:
        file = open('infos.txt', 'w', encoding='utf-8')
        for info in infos:
            file.write(info + '\n')
    except FileNotFoundError:
        print("File was not found")
        return None
    else:
        print('Infos were saved successfully')
        return 1
    finally:
        file.close()

# Bloc 2 ===============================================================================

def division(a, b):
    try:
        return a / b
    except TypeError:
        print('type error')
        raise
    except ZeroDivisionError:
        print('can not divide by zero')
        raise

class AgeVerification(Exception):
    @staticmethod
    def is_adult(age):
        if age < 18:
            raise AgeVerification("Not an adult")

def college(students):
    accepted_student = []

    for student in students:
        try:
            
            AgeVerification.is_adult(student['age'])
        except AgeVerification as e:
            print(e)
        else:
            accepted_student.append(student)
            print("Accepted")

    if accepted_student:
        return accepted_student
    return None


# Bloc 3 ===============================================================================

def save_to_file(infos):
    try:
        file = open('infos.txt', 'w', encoding='utf-8')
        
        for info in infos:
            if info:
                file.write(info + '\n')
        #with writelines i wouldn't need looping throught the infos
    except FileNotFoundError:
        print('File Not Found')
        return None
    else:
        print('Infos have saved successfully')
        return True
    finally:
        file.close()
        
        
def load_infos():
    try:
        with open('infos.txt', 'r', encoding='utf-8') as f:
            #read(): returns all the file content in one string
            #readline(): returns one line at a time
            #readlines(): return list of lines
            data = f.readlines()
            print(f.tell())
    except FileNotFoundError:
        print("File Not Found")
        return None
    else:
        print('Data has been loaded successfully')
        return data
            

# Bloc 4 ===============================================================================

def load_data():
    try:
        file = open('/etc/shadow', 'r')
        data = file.read()
    
    except FileNotFoundError:
        print('File Not Found')
        return None
    except PermissionError:
        print('You need permission for this action')
        return None
    else:
        print('Data loaded successfully')
        return data
    finally:
        file.close()

def read_csv():
    data = []
    
    try:
        with open('data.csv', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split(',')
                if len(line) != 5:
                    continue
                data.append(line)
    except FileNotFoundError:
        print('File not found')
        return None
    except PermissionError:
        print('Permission needed for this action')
        return None
    else:
        print('Data has been loaded successfully')
        return data
    finally:
        print('file closed with (with)')
                


def read_json():
    
    try:
        with open('inf.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)
    except FileNotFoundError as e:
        print(f'Error: {e}')
        return None
    except PermissionError:
        print('Permission needed for this action')
        return None
    else:
        print('json data loaded successfully')
        return json_data
    finally:
        print('File has been closed auto with (with)') # not oblg


# Mini Challenge

class UnknownProduct(Exception):
    pass



def order_manager(stock, orders):
    for order in orders:
        order = order.split(',')
        
        try:
            order[1] = int(order[1])
            if order[0] in stock:
                if order[1] <= stock[order[0]]:
                    stock[order[0]] -= order[1]
                    print(f'[OK] {order[0]} : -{order[1]} (rest{stock[order[0]]})')
                else:
                    raise ValueError
            else:
                raise UnknownProduct('Unknown product')
            
        except TypeError:
            print(f'[ERROR] {order[0]} : Invalid quantity ({order[1]})')
        except ValueError:
            print(f'[ERROR] {order[0]} : stock insuffisant (demande {order[1]}, dispo {stock[order[0]]})')
        except UnknownProduct as e:
            print(f'[ERROR] {order[0]} : {e}')
        except (KeyError, IndexError):
            print(f'[ERROR] {f"{order[0]} :" if order[0] else ""} Something is missing')
        


def main():

    # bloc 1:

    # try:
    #     age = int(input('Enter you age: '))
    # except Exception as e:
    #     print(e)
    # else:
    #     if verify_age(age):
    #         print(f"You're {age} yo\n")

    # infos = ['hafid has started a local business.', 'xxx have a something.', 'xxxxx revealed his secrete.']
    #
    # save_infos(infos)

    # bloc 2:

    # age = -2 
    # #just for testing
    # try:
    #     if age > 120 or age < 0:
    #         raise ValueError('Age out of range')
    # except Exception as e:
    #     print(f'Error: {e}')

    # try:
    #     division(12, '3')
    # except Exception:   #just to catch the exception from the function (division)
    #     print('there is an error on the division function')

    # age = -23

    # try:
    #     AgeVerification.is_adult(age)
    # except AgeVerification as e:
    #     print(e)

    #bloc 3:
    
    # infos = load_infos()
    
    #bloc 4:
    
    # data = load_data()
    
    # csv_data = read_csv()
    # print(csv_data)
    
    # if json_data := read_json():
    #     print(json_data)
    
    # mini challenge
    
    stock = {"pommes": 20, "bananes": 4, "oranges": 15}
    orders = commandes_brutes = [
                                    "pommes,5",
                                    "bananes,10",
                                    "kiwis,2",
                                    "oranges,abc",
                                    "oranges,5",
                                    ""
                                ]
    order_manager(stock, orders)


if __name__ == '__main__':
    main()