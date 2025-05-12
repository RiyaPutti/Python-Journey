birth_year = int(input("enter your birth year: "))
current_age = 2025
present_age = current_age - birth_year
print("you are",  present_age, "years old.")

'''
📌Concepts Covered:

input() → takes user input as a string

int() → typecasting to integer

Variables → used to store data

Arithmetic operator (-) → subtraction

🧠 Logic:

The user's birth year is taken via input() and converted to an integer.

The current year is hardcoded (could be made dynamic with datetime).

Age is calculated by subtracting birth_year from current_year.

print() displays the final result using string concatenation and/or formatting.'''