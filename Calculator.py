def calculator():
    # Define the core mathematical operations
    def add(n1, n2):
        return n1 + n2

    def subtract(n1, n2):
        return n1 - n2

    def multiply(n1, n2):
        return n1 * n2

    def divide(n1, n2):
        if n2 == 0:
            return "Error: Division by zero"
        return n1 / n2

    # Map symbols to their corresponding functions for dynamic lookups
    operation = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    # Prompt the user for the initial starting number
    num1 = float(input("Could you please enter the first number? \n"))

    # Display available operators to the user
    for operate in operation:
        print(operate)

    # Maintain the calculation loop based on user choice
    should_continue = True
    while should_continue:
        select_operation = input("Select operation from above: \n")
        num2 = float(input("What's the next number? \n"))
        
        # Retrieve the correct function from the dictionary and execute it
        selected_symbol = operation[select_operation]
        answer = selected_symbol(num1, num2)
        print(f"{num1} {select_operation} {num2} = {answer}\n")

        # Check if the user wants to keep chaining operations or reset
        user_choice = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation: ")
        if user_choice == "y":
            num1 = answer
        else:
            should_continue = False
            print("\n" * 20)  # Optional: Clears the screen visually for the new session
            calculator()

# Start the application
calculator()