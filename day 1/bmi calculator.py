height = float(input("enter your height (m) : "))
weight = float(input("Enter your weight (kg): "))
bmi = weight / (height ** 2)
print("Your BMI is", round(bmi, 2))

''' 
📌 Concepts Covered:

Exponentiation with **

Floating-point division

Function call (round())

🧠 Logic:

Takes two inputs: weight (kg) and height (meters).

Uses the BMI formula:
BMI = WEIGHT / (HEIGHT)^2
Uses round() to restrict the output to 2 decimal places.

Output is formatted using print().'''