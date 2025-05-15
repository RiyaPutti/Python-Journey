def gcd(a, b):
    """
    Function to return the GCD of two numbers using Euclidean algorithm.
    """
    while b != 0:
        a, b = b, a % b
    return a

# Get user input
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
print(f"The GCD of {x} and {y} is: {gcd(x, y)}")

'''
📌 Concepts Covered:
- Function with return value
- While loop for iteration
- Modulo operator for remainder calculation
- Tuple unpacking for swapping values
- User input handling

🧠 Logic:
The Euclidean algorithm is a method for computing the greatest common divisor (GCD) of two integers. It works by repeatedly replacing the larger number with the remainder of the division of the larger number by the smaller number until one of the numbers becomes zero. The other number at that point is the GCD.
in Python, we can implement this using a while loop and the modulo operator. The function takes two integers as input and returns their GCD. The user is prompted to enter two numbers, and the result is printed.
 in optimal time complexity of O(log(min(a, b))) and space complexity of O(1).
 keep replacing (a, b) with (b, a % b) until b becomes 0. The last non-zero value of a is the GCD.
 '''