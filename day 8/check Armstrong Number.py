def is_armstrong_number(num):
    # Convert the number to a string to iterate over digits
    str_num = str(num)
    # Calculate the number of digits
    num_digits = len(str_num)
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == num 

# Get user input
number = int(input("Enter a number: ")) 
print(f"Is {number} an Armstrong number? {is_armstrong_number(number)}")

'''
📌 Concepts Covered:
- Function with return value
- String manipulation
- Loop iteration
- List comprehension
- Mathematical operations
- User input handling

🧠 Logic:
An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153. We convert the number to a string to easily iterate over its digits, calculate the sum of each digit raised to the power of the number of digits, and check if it equals the original number.
'''