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
    
    while name := input("name: ").strip() == "":
        pass
    
    while surname := input("surname: ").strip() == "":
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
    
    
# pick a student for their average


    
 
 # show students=========================================================================
    
def show_students():
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
    print("3. Average of a student")
    print("4. Quit")




if __name__ == "__main__":
    main()