def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))

'''📌 Concepts Covered:

Recursion

Base case

🧠 Logic:
Function calls itself until it hits zero. Each step multiplies n with the factorial of n-1. Like nesting dolls but with math.'''