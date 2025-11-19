# Prompt the user for the two numbers
# We use float() to allow for decimal numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Prompt for the operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform the calculation using Match Case
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")

    case "-":
        result = num1 - num2
        print(f"The result is {result}")

    case "*":
        result = num1 * num2
        print(f"The result is {result}")

    case "/":
        # Special check: You cannot divide by zero!
        if num2 == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")

    # This handles any input that is not one of the four symbols above
    case _:
        print("Invalid operation selected.")