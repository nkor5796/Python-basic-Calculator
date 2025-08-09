# ✅ Simple Python Calculator with History and Loop

# History list to store past calculations
calculation_history = []

# Function to do basic arithmetic
def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return "Invalid operator"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# Function to show previous calculations
def show_history():
    if calculation_history:
        print("\n📘 Previous Calculations:")
        for entry in calculation_history:
            print(" -", entry)
    else:
        print("\n📭 No history yet.")

# Main function
def main():
    print("🔢 Welcome to the Simple Calculator!")
    print("Supported operations: +, -, *, /")

    while True:
        print("\nChoose an option:")
        print("1. New Calculation")
        print("2. View History")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter the second number: "))

                result = calculate(num1, num2, operator)
                print("✅ Result:", result)

                # Save to history
                record = f"{num1} {operator} {num2} = {result}"
                calculation_history.append(record)

            except ValueError:
                print("❌ Invalid input. Please enter numbers only.")

        elif choice == '2':
            show_history()

        elif choice == '3':
            print("👋 Exiting calculator. Goodbye!")
            break

        else:
            print("❗ Invalid option. Please choose 1, 2, or 3.")

# Start the program
if __name__ == "__main__":
    main()
