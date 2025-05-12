try:
    with open("missing.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Oops! File not found.")


'''📌 Concepts Covered:

try-except with files

Catching FileNotFoundError

🧠 Logic:
If the file doesn’t exist, Python won’t throw a tantrum — it politely tells you “nope.”'''