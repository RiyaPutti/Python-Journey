try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero, silly!")

'''
📌 Concepts Covered:

Handling specific exceptions

🧠 Logic:
Dividing by 0 is illegal in math and Python. The except block catches the error and says something human instead of throwing a tantrum.'''