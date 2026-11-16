
print("===== AREA CALCULATOR =====")
print("1. Area of Square")
print("2. Area of Rectangle")
print("3. Area of Circle")
print("4. Area of Triangle")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    side = float(input("Enter side: "))
    area = side * side
    print("Area of Square:", area)

elif choice == 2:
    length = float(input("Enter length: "))
    breadth = float(input("Enter breadth: "))
    area = length * breadth
    print("Area of Rectangle:", area)

elif choice == 3:
    radius = float(input("Enter radius: "))
    area = 3.14 * radius * radius
    print("Area of Circle:", area)

elif choice == 4:
    base = float(input("Enter base: "))
    height = float(input("Enter height: "))
    area = 0.5 * base * height
    print("Area of Triangle:", area)

else:
    print("Invalid choice!")
