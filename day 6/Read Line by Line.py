with open("notes.txt", "r") as file:
    for line in file:
        print("Line:", line.strip())

'''
📌 Concepts Covered:

File iteration

.strip() to remove \n

🧠 Logic:
You loop through the file line-by-line like a scroll reader. strip() just cleans it up.'''