sentence = input("Enter a sentence: ")
words = sentence.split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) + 1
    
    print(f"Word: {word}, Frequency: {freq[word]}")
    
# Print the frequency of each word
print("\nWord Frequencies:")
for word, count in freq.items():
    print(f"{word}: {count}")
# This code counts the frequency of each word in a given sentence.

'''
concepts:
1. Input: The program prompts the user to enter a sentence.
2. Splitting the sentence: The sentence is split into words using the `split()` method, which separates the words based on spaces.
3. Dictionary: A dictionary `freq` is created to store the frequency of each word.
4. Counting frequency: The program iterates through each word in the list of words. For each word, it updates the frequency count in the dictionary using the `get()` method, which returns the current count or 0 if the word is not already in the dictionary.
5. Printing frequency: After counting the frequencies, the program prints the frequency of each word in the sentence.

logic: 
1. The user is prompted to enter a sentence.
2. The sentence is split into words using the `split()` method.
3. A dictionary `freq` is created to store the frequency of each word.
4. The program iterates through each word in the list of words.
5. For each word, it updates the frequency count in the dictionary using the `get()` method.
6. Finally, the program prints the frequency of each word in the sentence.
'''