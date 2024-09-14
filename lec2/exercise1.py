class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add_student(self, name, grade):
        student = Student(name, grade)
        self.students.append(student)

    def print_student_info(self):
        for student in self.students:
            print(f"{student.name}: {student.grade}")

def main():
    database = StudentDatabase()

    while True:
        choice = input("Enter '1' to add new student info, '2' to print all information, or 'q' to quit: ")
        if choice == '1':
            name = input("Enter student name (or 'q' to quit): ")
            if name == 'q':
                break
            grade = input(f"Enter grade for {name}: ")
            database.add_student(name, grade)
        elif choice == '2':
            database.print_student_info()
        elif choice == 'q':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

# Example to demonstrate local and global variables

# Global variable
global_var = "I am a global variable"

def local_variable_example():
    # Local variable
    local_var = "I am a local variable"
    print(local_var)  # Output: I am a local variable

# Accessing global variable
print(global_var)  # Output: I am a global variable

# Accessing local variable outside the function will result in an error
# print(local_var)  # Uncomment this line to see the error

# Calling the function to access the local variable
local_variable_example()