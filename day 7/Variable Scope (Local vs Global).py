x = 10  # Global

def show():
    x = 5  # Local
    print("Inside function:", x)

show()
print("Outside function:", x)

'''
📌 Concepts Covered:

Variable scope (local and global)

🧠 Logic:
Inside the function, x = 5 is local. Outside, it’s still x = 10. They live in different apartments 🏢.'''