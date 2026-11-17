print("Simple Calculator")

while True:
    # Ask for the operation first so the user can quit here.
    operation = input("\nChoose an operation (+, -, *, /) or q to quit: ").strip()

    if operation.lower() == "q":
        print("Goodbye!")
        break

    if operation not in ("+", "-", "*", "/"):
        print("Please choose +, -, *, or /.")
        continue

    # float() lets us work with decimals as well as whole numbers.
    try:
        first = float(input("First number: "))
        second = float(input("Second number: "))
    except ValueError:
        print("That wasn't a valid number. Try again.")
        continue

    if operation == "+":
        result = first + second
    elif operation == "-":
        result = first - second
    elif operation == "*":
        result = first * second
    else:
        # Check before dividing to avoid a division-by-zero error.
        if second == 0:
            print("You can't divide by zero.")
            continue
        result = first / second

    print(f"Result: {result}")