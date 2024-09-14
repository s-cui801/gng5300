B = [1, 2, 3]
A = B

# Modifying A will also modify B
A.append(4)
print(B)  # Output: [1, 2, 3, 4]

B.append(5)
print(A)  # Output: [1, 2, 3, 4, 5]
A = [1, 2, 3]
B = [4, 5, 6]

# Using extend to add elements from B to A
A.extend(B)
print(A)  # Output: [1, 2, 3, 4, 5, 6]

# Using append to add B as a single element to A
A.append(B)
print(A)  # Output: [1, 2, 3, 4, 5, 6, [4, 5, 6]]

num = input("Enter a number: ")
if num > 0:
    print("Positive number")
else:
    if num == 0:
        print("Zero")
    else:
        if num < 0:
            print("Negative number")

            numbers = [1, 2, 3, 4, 5]
            for num in numbers:
                print(num)
                # Example 1: Using a for loop to iterate over a list
                fruits = ["apple", "banana", "orange"]
                for fruit in fruits:
                    print(fruit)

                # Example 2: Using a for loop with range to iterate over a sequence of numbers
                for i in range(1, 6):
                    print(i)

                # Example 3: Using a for loop with else to execute code when the loop completes normally
                numbers = [1, 2, 3, 4, 5]
                for num in numbers:
                    if num == 3:
                        break
                    print(num)
                else:
                    print("Loop completed normally")


# Function to add student names
def add_student_names():
    student_names = []
    while True:
        name = input("Enter student name (or 'q' to quit): ")
        if name == 'q':
            break
        student_names.append(name)
    return student_names

# Function to add student grades
def add_student_grades(student_names):
    student_grades = {}
    name = input("Enter the name of the student: ")
    if name not in student_grades:
        print(f"Adding {name} to the student list.")
    grade = input(f"Enter grade for {name}: ")
    student_grades[name] = grade
    return student_grades

# Function to print student information
def print_student_info(student_grades):
    for name, grade in student_grades.items():
        print(f"{name}: {grade}")

# Main program
names = add_student_names()
grades = add_student_grades(names)

while True:
    choice = input("Enter '1' to add new names, '2' to add grades, '3' to print all information, or 'q' to quit: ")
    if choice == '1':
        names.extend(add_student_names())
    elif choice == '2':
        grades.update(add_student_grades(names))
    elif choice == '3':
        print_student_info(grades)
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Please try again.")