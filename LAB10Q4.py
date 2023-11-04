# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Function to perform modulus
def modulus(a, b):
    if b == 0:
        return "Error: Modulus by zero"
    return a % b

# Function to perform exponentiation
def exponentiate(a, b):
    return a ** b

while True:
    print("Calculator Menu:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")

    choice = input("Enter your choice (1/2/3/4/5/6/7): ")

    if choice == '7':
        break

    try:
        a = float(input("Enter the first operand: "))
        b = float(input("Enter the second operand: "))

        if choice == '1':
            result = add(a, b)
        elif choice == '2':
            result = subtract(a, b)
        elif choice == '3':
            result = multiply(a, b)
        elif choice == '4':
            result = divide(a, b)
        elif choice == '5':
            result = modulus(a, b)
        elif choice == '6':
            result = exponentiate(a, b)
        else:
            print("Invalid choice. Please select a valid option (1-7).")
            continue

        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid operands (numeric values).")
    except ZeroDivisionError:
        print("Error: Division by zero.")