def reverse_string(s):
    """
    This function takes a string as input and returns the string reversed.
    
    :param s: str, the string to be reversed
    :return: str, the reversed string
    """
    return s[::-1]

text = input("Enter a string: ")
print(f"Reversed string: {reverse_string(text)}")

'''
📌 Concepts Covered:
- String slicing
- Function with return value
- User input handling
- String manipulation
🧠 Logic:
We use Python's slicing feature to reverse the string. The slice [::-1] means start from the end towards the first element, effectively reversing the string.
'''