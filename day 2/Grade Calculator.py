marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: C or below")

'''
📌 Concepts Covered:

elif (else if)

Priority-based condition checking

🧠 Logic:

It checks marks in descending order.

First condition to match gets executed (like a waterfall).'''