def main():
    
    listtt = [1,5,33,'hello', 5, -12, 200]
    
    if max := find_max(listtt):
        print(f'The max value is: {max}')

    if min := find_min(listtt):
        print(f'The min value is: {min}')
            
    if results := notes_above(listtt, 5):
        print(f'Notes above the bar are: {results}')
        
    if stats := occurrences_counter(listtt):
        for stat in stats:
            print(f'{stat}: {stats[stat]}')
        
    print(f'before inversion: {listtt}')   
    list_inverser(listtt)
    print(f'after inversion: {listtt}')
    
    print(merge_2_list([1, 4, 7], [2, 3, 8, 9]))
    
    #list comprehension  
    numbers = [3, 12, 7, 25, 8, 19, 2]
    
    res = [(n ** 2) for n in numbers if n % 2 == 0]
    
    print(res)
    
    
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
    
    while i1 != len(l1) or i2 != len(l2):
        
        if i1 != len(l1) and i2 != len(l2):
            
            if l1[i1] < l2[i2]:
                result.append(l1[i1])
                i1 = i1 + 1
                
            elif l1[i1] == l2[i2]:
                result.append(l1[i1])
                result.append(l2[i2])
                i1 = i1 + 1
                i2 = i2 + 1
            
            else:
                result.append(l2[i2])
                i2 = i2 + 1
        
        elif i1 != len(l1):
            
            for i in range(i1, len(l1)):
                result.append(l1[i])

            i1 = len(l1)
            
        else:
            
            for i in range(i2, len(l2)):
                result.append(l2[i])

            i2 = len(l2)
            
    return result





if __name__ == '__main__':
    main()