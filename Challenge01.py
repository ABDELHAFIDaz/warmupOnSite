STUDENTS = []

def main():
    
    while True:
        show_menu()
        
        user_input = input("Choose: ")
        
        match(user_input):
            case '1':
                add_student()
            case '2':
                show_students()
            case '3':
                appreciation()
            case '4':
                print("That's all for this time")
                break

# average note===============================================================================

def calcule_average(student):
    sum = 0
    note_counter = 0
    
    for note in student['notes']:
        sum = sum + note
        note_counter = note_counter + 1
     
    if note_counter == 0:
         return
     
    average = sum / note_counter
    
    return average


# when adding a student======================================================================

def add_student() -> None:
    while (name := input("name: ")).strip() == "":
        pass
    
    while (surname := input("surname: ")).strip() == "":
        pass
    
    notes = []
    
    note_counter = 1
    
    while len(notes) < 3:
        try:
            
            while not (0 <= (note := int(input(f'note ^{note_counter}: '))) <= 20):
                pass
            
        except ValueError:
            print("Only numbers, you gotta start over again\n")
            return
        
        notes.append(note)
        note_counter = note_counter + 1
    
    student = {
        'name': name,
        'surname': surname,
        'notes': notes
        }
    
    STUDENTS.append(student)
    print(f'{student['name']} is successfully added')
    
    
# appreciation=============================================================================================

def appreciation():
    
    if is_students_empty(): return
    
    print("\n=========================================")
    print("        STUDENTS-APPRECIATION       ")
    print("=========================================\n")
    
    best_students = []
    worst_students = []
    max = -1
    min = 21
    
    for student in STUDENTS:
        
        average = calcule_average(student)
        
        
        if not (0 > average or average > 20):
            if average > max:
                best_students = [student['name']]
                max = average
            elif average < min:
                worst_students = [student['name']]
                min = average
            elif average == max:
                best_students.append(student['name'])
            elif average == min:
                worst_students.append(student['name'])
                
        
        if 0 <= average < 10:
            print(f"{student['name']} {student['surname']} -> {average} -> Fail")
        elif 10 <= average < 12:
            print(f"{student['name']} {student['surname']} -> {average} -> Pass")
        elif 12 <= average < 16:
            print(f"{student['name']} {student['surname']} -> {average} -> Good")
        elif 16 <= average < 20:
            print(f"{student['name']} {student['surname']} -> {average} -> Very Good")
        else:
            print(f"{student['name']} {student['surname']} -> {average} -> Off range")
            
    
    if best_students:
        print("Best student(s):", end="")
        for std in best_students:
            print(std, end=", ")
            
    print()
          
    if worst_students:
        print("Worst student(s):", end="")
        for std in worst_students:
            print(std, end=", ")

    
 
 # show students=========================================================================
    
def show_students():
    
    if is_students_empty(): return
    
    print("=========================================")
    print("        STUDENT-AVERAGE       ")
    print("=========================================\n")
        
    for student in STUDENTS:
        print(f"{student['name']} {student['surname']} with the average of: {calcule_average(student)}\n")
    
# menu=============================================================================
    
def show_menu():

    print("=========================================")
    print("        STUDENTS MANAGER - MAIN MENU       ")
    print("=========================================")
    print("1. Add a student")
    print("2. Show all students")
    print("3. Appreciation of all student")
    print("4. Quit")


def is_students_empty():
    if len(STUDENTS) == 0:
        print("============================================================================")
        print("        THERE IS NO STUDENT IN THE SYSTEM NOW, (press 1 to add one)      ")
        print("============================================================================\n")
        return True
    
    return False


if __name__ == "__main__":
    main()