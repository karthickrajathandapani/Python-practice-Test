def cal(a, b, choice):
    if choice == 1:
        print("Add:", a + b)
    elif choice == 2:
        print("Sub:", a - b)
    elif choice == 3:
        print("Mul:", a * b)
    elif choice == 4:
        if b != 0:
            print("Div:", a / b)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid choice")

a = int(input("Enter first value: "))
b = int(input("Enter second value: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice: "))

cal(a, b, choice)
