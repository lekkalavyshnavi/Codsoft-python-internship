import random
import string

def generate_password():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the desired length of the password: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
        
        print("Choose the complexity level:")
        print("1. Letters only")
        print("2. Letters and numbers")
        print("3. Letters, numbers, and special characters")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            characters = string.ascii_letters
        elif choice == "2":
            characters = string.ascii_letters + string.digits
        elif choice == "3":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid choice! Please select a valid option.")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a numeric value for the length.")

if __name__ == "__main__":
    generate_password()

