
# Student Grading System

students = []

def add_student():
    name = input("Enter student name: ")

    marks = []

    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    students.append(student)

    print("Student added successfully!")


def view_students():
    if len(students) == 0:
        print("No student records found!")

    else:
        for student in students:
            print("\n===== STUDENT RESULT =====")
            print("Name:", student["name"])
            print("Marks:", student["marks"])
            print("Total:", student["total"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])


def search_student():
    name = input("Enter student name: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("\nStudent Found!")
            print("Name:", student["name"])
            print("Average:", student["average"])
            print("Grade:", student["grade"])
            return

    print("Student not found!")


while True:

    print("\n===== STUDENT GRADING SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")
