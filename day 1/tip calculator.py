bill = float(input("Enter the total bill: "))
tip_percent = float(input("Enter tip %: "))
tip = (tip_percent / 100) * bill
print("Tip amount:", tip)

'''
📌 Concepts Covered:

Floating-point arithmetic for precision

Basic percentage calculation

Operator precedence

🧠 Logic:

Takes bill and tip_percent as float inputs.

Calculates tip using the formula:

tip = (tip_percent/100) x bill

Outputs the result with basic formatting using print().'''