# Calculator program with 6 arithmetic operations
# Implemented by Alireza Khaleghi - Alrezakhaleghi@gmail.com

import re

def calculate(expression):
    """Calculate the value of a given expression"""
    # Remove whitespace from the expression
    expression = re.sub(r'\s+', '', expression)

    # Create a list of the operators in the expression
    operators = re.findall(r'[\+\-\*/\(\)]', expression)

    # Check that the expression is well-formed
    if not all(operator in '+-*/()' for operator in operators):
        raise ValueError("Invalid expression")

    # Evaluate the expression using the order of operations
    # First, evaluate expressions inside parentheses
    while '(' in expression:
        m = re.search(r'\(([^()]*)\)', expression)
        if not m:
            raise ValueError("Invalid expression")
        inner_expression = m.group(1)
        inner_value = calculate(inner_expression)
        expression = expression.replace(f"({inner_expression})", str(inner_value))

    # Next, evaluate exponentiation
    while '**' in expression:
        m = re.search(r'([\d\.]+)\*\*([\d\.]+)', expression)
        if not m:
            raise ValueError("Invalid expression")
        base = float(m.group(1))
        exponent = float(m.group(2))
        value = base ** exponent
        expression = expression.replace(m.group(0), str(value))

    # Then, evaluate multiplication and division from left to right
    while any(op in expression for op in '*/'):
        m = re.search(r'([\d\.]+)([\*/])([\d\.]+)', expression)
        if not m:
            raise ValueError("Invalid expression")
        left = float(m.group(1))
        operator = m.group(2)
        right = float(m.group(3))
        if operator == '*':
            value = left * right
        else:
            if right == 0:
                raise ValueError("Cannot divide by zero")
            value = left / right
        expression = expression.replace(m.group(0), str(value))

    # Finally, evaluate addition and subtraction from left to right
    while any(op in expression for op in '+-'):
        m = re.search(r'([\d\.]+)([\+\-])([\d\.]+)', expression)
        if not m:
            raise ValueError("Invalid expression")
        left = float(m.group(1))
        operator = m.group(2)
        right = float(m.group(3))
        if operator == '+':
            value = left + right
        else:
            value = left - right
        expression = expression.replace(m.group(0), str(value))

    # The final value of the expression is the result
    return float(expression)

print("Welcome to the calculator program!")

while True:
    # Take input from the user
    expression = input("\nEnter an expression to calculate, or 'quit' to exit: ")

    # Exit the program if user chooses to quit
    if expression == 'quit':
        print("Thanks for using the calculator program! Goodbye.")
        break

    # Calculate the value of the expression
    try:
        result = calculate(expression)
        print(f"{expression} = {result}")
    except ValueError as e:
        print(str(e))
