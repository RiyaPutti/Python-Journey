def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
print(f"{num} is prime? {is_prime(num)}")

''' 
📌 Concepts Covered:

Function with return value

Range and loop iteration

Optimization using square root

Modulo operator for divisibility check

🧠 Logic:
A prime number is divisible only by 1 and itself. Instead of checking up to n-1, we optimize by checking till √n as a factor beyond that would have a corresponding smaller factor already checked.'''