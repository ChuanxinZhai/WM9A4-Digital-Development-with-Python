
# calculator 2.

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculator():
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4):")

    #限定输入的值必须为 1/2/3/4
    # restrict the input value must be 1/2/3/4
    while choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        choice = input("Enter choice (1/2/3/4):")

    if choice == "1":
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(add(num1, num2))

    elif choice == "2":
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(subtract(num1, num2))

    elif choice == "3":
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(multiply(num1, num2))

    else:
        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))
        print(divide(num1, num2))


calculator()
