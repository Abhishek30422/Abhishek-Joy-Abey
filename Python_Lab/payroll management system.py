
import csv
import os

FILE_NAME = "employees.csv"


# Create CSV file if it does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "ID", "Name", "Basic Salary",
                "Allowance", "Deduction", "Net Salary"
            ])


# Add employee
def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")

    basic = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    deduction = float(input("Enter Deduction: "))

    net_salary = basic + allowance - deduction

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            emp_id, name, basic,
            allowance, deduction, net_salary
        ])

    print("Employee added successfully!")


# View all employees
def view_employees():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\n===== EMPLOYEE DETAILS =====")

        found = False

        for employee in reader:
            found = True
            print("Employee ID:", employee["ID"])
            print("Name:", employee["Name"])
            print("Basic Salary:", employee["Basic Salary"])
            print("Allowance:", employee["Allowance"])
            print("Deduction:", employee["Deduction"])
            print("Net Salary:", employee["Net Salary"])
            print("------------------------")

        if not found:
            print("No employee records found!")


# Search employee
def search_employee():
    emp_id = input("Enter Employee ID to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            if employee["ID"] == emp_id:
                print("\nEmployee Found!")
                print("Name:", employee["Name"])
                print("Net Salary:", employee["Net Salary"])
                return

    print("Employee not found!")


# Generate salary slip
def salary_slip():
    emp_id = input("Enter Employee ID: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for employee in reader:
            if employee["ID"] == emp_id:
                print("\n===== SALARY SLIP =====")
                print("Employee ID:", employee["ID"])
                print("Employee Name:", employee["Name"])
                print("Basic Salary:", employee["Basic Salary"])
                print("Allowance:", employee["Allowance"])
                print("Deduction:", employee["Deduction"])
                print("------------------------")
                print("Net Salary:", employee["Net Salary"])
                print("========================")
                return

    print("Employee not found!")


# Main program
create_file()

while True:

    print("\n===== PAYROLL MANAGEMENT SYSTEM =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Generate Salary Slip")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employees()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        salary_slip()

    elif choice == "5":
        print("Thank you for using Payroll Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
