def find_max_of_three(a, b, c):
    """
    This function takes three numbers as input and returns the maximum of the three.
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
x = int(input("Enter first number: "))
y = int(input("Enter second number: ")) 
z = int(input("Enter third number: "))
print(f"The max is: {find_max_of_three(x, y, z)}") 

'''
📌 Concepts Covered:

Conditional statements (if, elif, else)

Function with multiple parameters

Relational operators

🧠 Logic:
We perform pairwise comparisons using >= to evaluate which of the three numbers is greatest and return the largest one accordingly.'''