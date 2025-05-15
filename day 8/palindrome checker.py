def palindrome_checker(s):
    """
    Check if a string is a palindrome.
    A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).
    """
    # Normalize the string: remove spaces and convert to lowercase
    
    s= s.lower().replace(" ", "")
    # Check if the string is equal to its reverse   
    return s == s[::-1]
# Get user input
string = input("Enter a string: ")
print(f"Is the string a palindrome? {palindrome_checker(string)}")

'''
📌 Concepts Covered:
- String manipulation
- Function with return value
- String slicing
- User input handling
- Conditional logic
🧠 Logic:
We first normalize the string by converting it to lowercase and removing spaces. Then we check if the string is equal to its reverse using slicing. If they are equal, the string is a palindrome.
'''