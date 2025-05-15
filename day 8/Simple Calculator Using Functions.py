def calculator(a, b, op):
    """
    This function takes two numbers and an operator as input and returns the result of the operation.
    """
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        return a / b
    else:
        return "Invalid operator"
    
# Get user input 

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))   
op = input("Enter operator (+, -, *, /): ")
print(f"Result : {calculator(x, y, op)}")

'''
📌 Concepts Covered:

Function with conditional logic

Error handling (division by zero)

Basic arithmetic operators

Typecasting user input

🧠 Logic:
Takes two numeric inputs and an operator symbol, then routes to the corresponding arithmetic operation using conditional branches. Includes edge case handling for division by zero.'''
