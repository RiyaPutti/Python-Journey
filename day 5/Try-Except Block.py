try:
    num = int("qwerty")
except ValueError:
    print("Oops! That’s not a number.")

'''📌 Concepts Covered:

Exception handling with try and except

🧠 Logic:
Python tries to convert "hello" to an integer, which fails. Instead of crashing, it shows a friendly error message.'''