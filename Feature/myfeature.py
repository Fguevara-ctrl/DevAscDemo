# myfeature.py

def greet(name):
    """Greets the user by name."""
    print(f"Hello, {name}! Welcome to Python programming.")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greet(user_name)