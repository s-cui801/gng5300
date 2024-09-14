# Function to add student names and grades
def add_student_info():
    student_info = {}
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name == 'q':
            break
        grade = input(f"Enter grade for {name}: ")
        student_info[name] = grade
    return student_info

# Function to print student information
def print_student_info(student_info):
    for name, grade in student_info.items():
        print(f"{name}: {grade}")

# Main program
info = add_student_info()

while True:
    choice = input("Enter '1' to add new student info, '2' to print all information, or 'q' to quit: ")
    if choice == '1':
        info.update(add_student_info())
    elif choice == '2':
        print_student_info(info)
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.")
