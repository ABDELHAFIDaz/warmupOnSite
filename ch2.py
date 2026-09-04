# bloc 1 =============================================================
    
def find_max(list):

    if len(list) == 0: return

    max = float('-inf')
    
    for ele in list:
        try:
            if ele > max:
                max = ele

        except TypeError:
            continue
    
    return max



def find_min(list):

    if len(list) == 0: return

    min = float('+inf')
    
    for ele in list:
        try:
            if ele < min:
                min = ele
                
        except TypeError:
            continue
    
    return min



def notes_above(notes, bar):
    if len(notes) == 0 or not (type(bar) == type(2) or type(bar) == type(2.2)) or not (0 <= bar <= 20): return
    
    results = []
    
    for note in notes:
        try:
            if note >= bar:
                results.append(note)
        except TypeError:
            continue
    
    return results



def occurrences_counter(list):
    
    if len(list) == 0: return
    
    stats = {}
    
    for item in list:
        
        is_exist = False
        
        for ele in stats:
            
            if item == ele:
                stats[ele] = stats[ele] + 1
                is_exist = True
                break
        
        if not is_exist:
            stats[item] = 1

    return stats


def list_inverser(list) -> None:
    
    if len(list) == 0: return
    
    if len(list) == 1: return list
        
    first_index = 0
    last_index = len(list) - 1
    
    while first_index != last_index:
        
        temp = list[first_index]
        list[first_index] = list[last_index]
        list[last_index] = temp
        
        first_index = first_index + 1
        last_index = last_index - 1


def sort_list(list):
    
    for i in range(len(list)):
        for u in range(len(list) - i):
            if i > u:
                temp = i
                i = u
                u = temp


def merge_2_list(l1, l2):
    result = []
    
    i1 = 0
    i2 = 0
    
    while i1 < len(l1) and i2 < len(l2):
           
        if l1[i1] <= l2[i2]:
            result.append(l1[i1])
            i1 = i1 + 1
            
        else:
            result.append(l2[i2])
            i2 = i2 + 1
    
    result.extend(l1[i1:]) 
    result.extend(l2[i2:]) 
            
    return result


# Bloc 2 ========================================================================

def sell(stock, product, quantity):
    
    try:
        if quantity < 1:
            print('quantity must be more than 0')
            return
        elif quantity > stock[product]:
            print(f'Stock is insufficient for {product} (disponible : {stock[product]})')
            return
        else:
            stock[product] = stock[product] - quantity
            print(f"Selled: {quantity} {product}")
    
    except TypeError:
        print("Type Error")
    
    except KeyError:
        print(f"{product} is not in stock")
    
    return


def out_of_stock(stock):
    
    result = []
    
    for product in stock:
        if stock[product] == 0:
            result.append(product)

    match len(result):
        case 0:
            return
        case 1:
            return result[0]
        case _:
            return result
        

def total_per_client(orders):
    
    stats = {}
    
    for order in orders:
        
        is_exist = False
        
        for client in stats:
            
            if order['client'] == client:
                stats[client] = stats[client] + order['quantity']
                is_exist = True
                break
        
        if not is_exist:
            stats[order['client']] = order['quantity']
            
    return stats


def dict_inverser(dict):
    
    tpl = list(dict.items())
    inversed_dict = {}
    
    for pair in tpl:
        inversed_dict[pair[1]] = pair[0]
    
    return inversed_dict


def dict_stats(dict):
    
    for key in dict:
        print(f'{key} : {len(dict[key])} employe(s)')
        
        
# Bloc 3 ===================================================================================================
        
def set_joins(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    
    print(f"subsribe in two courses: {set1 & set2}")
    print(f"subsribed in atleast one course: {set1 | set2}")
    print(f"Uniquely Python: {set1 - set2}")
    

def has_duplicates(list):
    
    sett = set(list)
    
    if len(list) == len(sett):
        return False
    
    return True



def nested_list_to_set(list):
    unique = set()
    
    for ele in list:
        unique.update(ele)
        
    return unique



# Bloc 4 ==================================================================================


def sells_stats(sells):
    
    total_per_product = {}
    best_seller = ""
    Produits_distincts = set()
    
    for sell in sells:
        for product in total_per_product:
            if sell['produit'] == product:
                total_per_product[product] = total_per_product[product] + sell['montant']




def main():
    
    listtt = [1,5,33,'hello', 5, -12, 200]
    
    # if max := find_max(listtt):
    #     print(f'The max value is: {max}')

    # if min := find_min(listtt):
    #     print(f'The min value is: {min}')
            
    # if results := notes_above(listtt, 5):
    #     print(f'Notes above the bar are: {results}')
        
    # if stats := occurrences_counter(listtt):
    #     for stat in stats:
    #         print(f'{stat}: {stats[stat]}')
        
    # print(f'before inversion: {listtt}')   
    # list_inverser(listtt)
    # print(f'after inversion: {listtt}')
    
    # print(merge_2_list([1, 4, 7], [2, 3, 8, 9]))
    
    # #list comprehension  
    # numbers = [3, 12, 7, 25, 8, 19, 2]
    
    # res = [(n ** 2) for n in numbers if n % 2 == 0]
    
    # print(res)
    
    #bloc 2:
    
    # stock = {"apples": 50, "bananas": 30, "oranges": 0}
    
    # sell(stock, 'apple', 10)

    # if out_stock := out_of_stock(stock):
    #     print(f'Product(s) that are out of stock: {out_stock}')
        
    # orders = [
    #             {"client": "Ali", "product": "apples", "quantity": 5},
    #             {"client": "Sara", "product": "bananas", "quantity": 10},
    #             {"client": "Ali", "product": "oranges", "quantity": 2},
    #         ]
    
    # if statistics := total_per_client(orders):
    #     print(statistics)
    
    # d = {"a": 1, "b": 2, "c": 3}
    
    # if inversed_d := dict_inverser(d):
    #     print(f'before: {d}')
    #     print(f'after: {inversed_d}')
    
    # words = ["chat", "elephant", "abeille", "riz"]
    
    # word_char = {w:len(w) for w in words}
    # print(word_char)
    
    # entreprise = {
    #                 "IT": ["Ali", "Sara", "Omar"],
    #                 "RH": ["Lina"],
    #                 "Ventes": ["Karim", "Yasmine", "Nadia", "Hicham"],
    #             }
    
    # dict_stats(entreprise)
    
    # bloc 3
    
    # atelier_python = ["Ali", "Sara", "Lina", "Karim"]
    # atelier_java = ["Sara", "Omar", "Lina", "Yasmine"]
    
    # set_joins(atelier_python, atelier_java)
    
    # liste_1 = ["Ali", "Sara", "Lina"]
    # liste_2 = ["Ali", "Sara", "Ali"]
    
    # print(f"a_des_doublons(liste_1) -> {"True" if has_duplicates(liste_1) else "False"}")
    # print(f"a_des_doublons(liste_2) -> {"True" if has_duplicates(liste_2) else "False"}")


    # tags_articles = [
    #                     ["python", "web", "api"],
    #                     ["python", "data"],
    #                     ["web", "css"],
    #                 ]
    
    # print(nested_list_to_set(tags_articles))
    
    # bloc 4:
    
    ventes = [
                {"produit": "pommes", "montant": 120},
                {"produit": "bananes", "montant": 80},
                {"produit": "pommes", "montant": 45},
                {"produit": "oranges", "montant": 60},
                {"produit": "bananes", "montant": 30},
            ]


    
if __name__ == '__main__':
    main()