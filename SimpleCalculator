# Calculator program with 6 arithmetic operations
# Implemented by Alireza Khaleghi - Alrezakhaleghi@gmail.com

def add(a, b):
    # Add two numbers
    return a + b

def subtract(a, b):
    # Subtract two numbers
    return a - b

def multiply(a, b):
    # Multiply two numbers
    return a * b

def divide(a, b):
    # Divide two numbers
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def exponentiate(a, b):
    # Raise a to the power of b
    return a ** b

def modulus(a, b):
    # Return the remainder of a divided by b
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a % b

print("Welcome to the calculator program!")

while True:
    print("\nPlease select an operation:\n" 
          "1. Addition\n" 
          "2. Subtraction\n" 
          "3. Multiplication\n" 
          "4. Division\n" 
          "5. Exponentiation\n"
          "6. Modulus\n"
          "7. Quit\n")

    # Take input from the user
    choice = input("Enter the number of your choice: ")

    # Exit the program if user chooses to quit
    if choice == '7':
        print("Thanks for using the calculator program! Goodbye.")
        break

    # Get the user's numbers for the selected operation
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

    # Perform the selected operation
    if choice == '1':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")

    elif choice == '4':
        try:
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        except ValueError as e:
            print(str(e))
            continue

    elif choice == '5':
        result = exponentiate(num1, num2)
        print(f"{num1} ** {num2} = {result}")

    elif choice == '6':
        try:
            result = modulus(num1, num2)
            print(f"{num1} % {num2} = {result}")
        except ValueError as e:
            print(str(e))
            continue

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")

