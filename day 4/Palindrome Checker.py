def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("madam"))

'''
📌 Concepts Covered:

Function with string input

Comparison using ==

String slicing

🧠 Logic:

A palindrome reads the same forwards and backwards.

Reversing and comparing the word tells us if it's a palindrome.'''