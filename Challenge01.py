STUDENTS = [
    {"name": "Karim", 'surname': 'go', "notes": [12, 15, 9]},
    {"name": "Sara", 'surname': 'to', "notes": [18, 17, 16]},
    {"name": "Lina", 'surname': 'ro', "notes": [6, 8, 5]},
]

# def main():
    
#     while True:
#         show_menu()
        
#         user_input = input("Choose: ")
        
#         match(user_input):
#             case '1':
#                 add_student()
#             case '2':
#                 show_students()
#             case '3':
#                 appreciation()
#             case '4':
#                 print("That's all for this time")
#                 break

# # average note===============================================================================

# def calcule_average(student):
#     sum = 0
#     note_counter = 0
    
#     for note in student['notes']:
#         sum = sum + note
#         note_counter = note_counter + 1
     
#     if note_counter == 0:
#          return
     
#     average = sum / note_counter
    
#     return average


# # when adding a student======================================================================

# def add_student() -> None:
#     while (name := input("name: ")).strip() == "":
#         pass
    
#     while (surname := input("surname: ")).strip() == "":
#         pass
    
#     notes = []
    
#     note_counter = 1
    
#     while len(notes) < 3:
#         try:
            
#             while not (0 <= (note := int(input(f'note ^{note_counter}: '))) <= 20):
#                 pass
            
#         except ValueError:
#             print("Only numbers, you gotta start over again\n")
#             return
        
#         notes.append(note)
#         note_counter = note_counter + 1
    
#     student = {
#         'name': name,
#         'surname': surname,
#         'notes': notes
#         }
    
#     STUDENTS.append(student)
#     print(f'{student['name']} is successfully added')
    
    
# # appreciation=============================================================================================

# def appreciation():
    
#     if is_students_empty(): return
    
#     print("\n=========================================")
#     print("        STUDENTS-APPRECIATION       ")
#     print("=========================================\n")
    
#     best_students = []
#     worst_students = []
#     max = -1
#     min = 21
    
#     for student in STUDENTS:
        
#         average = calcule_average(student)
        
        
#         if not (0 > average or average > 20):
#             if average > max:
#                 best_students = [student['name']]
#                 max = average
#             elif average < min:
#                 worst_students = [student['name']]
#                 min = average
#             elif average == max:
#                 best_students.append(student['name'])
#             elif average == min:
#                 worst_students.append(student['name'])
                
        
#         if 0 <= average < 10:
#             print(f"{student['name']} {student['surname']} -> {average:.2f} -> Fail")
#         elif 10 <= average < 12:
#             print(f"{student['name']} {student['surname']} -> {average:.2f} -> Pass")
#         elif 12 <= average < 16:
#             print(f"{student['name']} {student['surname']} -> {average:.2f} -> Good")
#         elif 16 <= average < 20:
#             print(f"{student['name']} {student['surname']} -> {average:.2f} -> Very Good")
#         else:
#             print(f"{student['name']} {student['surname']} -> {average:.2f} -> Off range")
            
    
#     if best_students:
#         print("Best student(s):", end="")
#         for std in best_students:
#             print(std, end=", ")
            
#     print()
          
#     if worst_students:
#         print("Worst student(s):", end="")
#         for std in worst_students:
#             print(std, end=", ")

    
 
#  # show students=========================================================================
    
# def show_students():
    
#     if is_students_empty(): return
    
#     print("=========================================")
#     print("        STUDENT-AVERAGE       ")
#     print("=========================================\n")
        
#     for student in STUDENTS:
#         print(f"{student['name']} {student['surname']} with the average of: {calcule_average(student):.2f}\n")
    
# # menu=============================================================================
    
# def show_menu():

#     print("=========================================")
#     print("        STUDENTS MANAGER - MAIN MENU       ")
#     print("=========================================")
#     print("1. Add a student")
#     print("2. Show all students")
#     print("3. Appreciation of all student")
#     print("4. Quit")


# def is_students_empty():
#     if len(STUDENTS) == 0:
#         print("============================================================================")
#         print("        THERE IS NO STUDENT IN THE SYSTEM NOW, (press 1 to add one)      ")
#         print("============================================================================\n")
#         return True
    
#     return False




#============================================= start again ====================================================


def main():
    
    #m1:
    
    # if student := add_student():
    
    #     if student_s_average := calculate_average(student['notes']):
            
    #         print(f"{student['name']}: {student_s_average:.2f}")
    
    #m2
    
    # for std in STUDENTS:
        
    #     if average := calculate_average(std['notes']):
    #         print(f"{average:.2f} -> {appreciation(average)}")
    
    # if students_stats := top_bottom_notes(STUDENTS):
        
    #     for key in students_stats:
            
    #         print(f"{key} are: ", end="")
            
    #         for std in students_stats[key]:
    #             print(std, end=", ")
            
    #         print()   
    
    #m3
    
    results = constract_results(STUDENTS)
    print(len(results))
    
    
    

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
    
    # STUDENTS.append(student)
    print(f'{student['name']} is successfully added')
    return student
    
    

def calculate_average(notes):
    
    if len(notes) == 0:
        print("notes is empty\n")
        return
     
    sum = 0
    
    for note in notes:  sum = sum + note
    try:   
        average = sum / len(notes)
        return average
    
    except ZeroDivisionError:
        print("There is no notes\n")
        return





def appreciation(average) -> str:
    
    if 0 <= average < 10:
        return "Fail"
    elif 10 <= average < 12:
        return "Pass"
    elif 12 <= average < 16:
        return "Good"
    elif 16 <= average < 20:
        return "Very good"
    else:
        return "Off range"
    
    
    

def top_bottom_notes(students):
    
    if len(students) < 2:
        return
    
    top_note = -1
    bottom_note = 21
    best_students = []
    worst_students = []
    
    for student in students:
        
        average = calculate_average(student['notes'])
        
        if top_note < average <= 20:
            top_note = average
            best_students = [student['name']]
                
        elif top_note == average:
            best_students.append(student['name'])
                
        if 0 <= average < bottom_note:
            bottom_note = average
            worst_students = [student['name']]
            
        elif bottom_note == average:
            worst_students.append(student['name'])
    
    return {
            'best_students': best_students,
            'worst_students': worst_students
        }
    
    
# def sort_by_average(resutls):
    
#     i = 0
    
#     while i < len(resutls):
        
        
        
#         i = i + 1
    
        
def constract_results(students):
    
    results = {}
    
    for student in students:
        
        if average := calculate_average(student['notes']):
            mention = appreciation(average)
            
            results[student['name']] = {'average': average, 'mention': mention}
    
    return results
    




def etudiants_en_echec(resultats):
    pass
def calculer_moyenne_ponderee(notes, coefficients):
    pass  # bonus
def regrouper_par_mention(resultats) :
    pass                # bonus
def moyenne_groupe(etudiants):
    pass                         # bonus
def somme_recursive(notes) :
    pass                           # bonus



if __name__ == "__main__":
    main()