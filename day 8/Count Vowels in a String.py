def count_vowels(s):
    """
    Count the number of vowels in a given string.

    Args:
    s (str): The input string.

    Returns:
    int: The count of vowels in the string.
    """
    vowels = set("aeiouAEIOU")
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
print(f"Number of vowels in the string: {count_vowels(text)}")


'''
📌 Concepts Covered:
- Function with return value
- Set for membership testing
- Loop iteration
- String manipulation 
- User input handling
🧠 Logic:
We define a set of vowels and iterate through each character in the string. If the character is found in the set, we increment the count. Finally, we return the total count of vowels.
'''