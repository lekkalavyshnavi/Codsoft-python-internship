def calculator():
    while True:
        print("\nSimple Calculator")
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "5":
            print("Exiting the calculator. Goodbye!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice! Please select a valid operation.")
            continue

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "1":
                result = num1 + num2
                operation = "+"
            elif choice == "2":
                result = num1 - num2
                operation = "-"
            elif choice == "3":
                result = num1 * num2
                operation = "*"
            elif choice == "4":
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                operation = "/"

            print(f"The result of {num1} {operation} {num2} is: {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

if __name__ == "__main__":
    calculator()
