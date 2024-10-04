def cal():
    while True:
        print("Simple Arithmetic Calculator")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = int(input("Enter your choice (1/2/3/4): "))

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result: ", num1 + num2)
        elif choice == 2:
            print("Result: ", num1 - num2)
        elif choice == 3:
            print("Result: ", num1 * num2)
        elif choice == 4:
            if num2 != 0:
                print("Result: ", num1 / num2)
            else:
                print("Error! Division by zero is not allowed.")
        else:
            print("Invalid choice.")

        use_again = input("Do you want to use the calculator again? (yes/no): ")
        if use_again.lower() != "yes":
            break
cal()
