
# Student Data Manager using File Handling

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open("students.txt", "a") as file:
        file.write(f"{roll},{name},{age},{course}\n")

    print("Student added successfully!")


def view_students():
    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

            if not records:
                print("No student records found!")
                return

            print("\n===== STUDENT RECORDS =====")

            for record in records:
                roll, name, age, course = record.strip().split(",")
                print("Roll Number:", roll)
                print("Name:", name)
                print("Age:", age)
                print("Course:", course)
                print("----------------------")

    except FileNotFoundError:
        print("Student file does not exist!")


def search_student():
    roll = input("Enter Roll Number to search: ")

    try:
        with open("students.txt", "r") as file:
            for record in file:
                data = record.strip().split(",")

                if data[0] == roll:
                    print("Student Found!")
                    print("Roll Number:", data[0])
                    print("Name:", data[1])
                    print("Age:", data[2])
                    print("Course:", data[3])
                    return

        print("Student not found!")

    except FileNotFoundError:
        print("Student file does not exist!")


def update_student():
    roll = input("Enter Roll Number to update: ")

    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        updated = False

        with open("students.txt", "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0] == roll:
                    name = input("Enter new name: ")
                    age = input("Enter new age: ")
                    course = input("Enter new course: ")

                    file.write(f"{roll},{name},{age},{course}\n")
                    updated = True
                else:
                    file.write(record)

        if updated:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("Student file does not exist!")


def delete_student():
    roll = input("Enter Roll Number to delete: ")

    try:
        with open("students.txt", "r") as file:
            records = file.readlines()

        deleted = False

        with open("students.txt", "w") as file:
            for record in records:
                data = record.strip().split(",")

                if data[0] == roll:
                    deleted = True
                else:
                    file.write(record)

        if deleted:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    except FileNotFoundError:
        print("Student file does not exist!")


while True:

    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you for using Student Data Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
