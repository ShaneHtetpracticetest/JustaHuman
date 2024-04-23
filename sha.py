# print("Welcome to Xaiver Club")
# username = input("Fill your name : ")
# print("Welcome Mr." , username )
# age = int(input("Enter your age : "))

# if age >= 18:
#     print("Welcome to Xaiver Club and enjoy it")

# else:
#     print("Get the fk out of here and come back when you are 18")


print("""                

        Welcome from SHA's calculation 

""")
while True:
    print("Enter the operation you want to perform (+, -, *, /) or 'quit' to exit:")
    
    operation = input("Operation: ")

    if operation.lower() == 'quit':
        print("Exiting the calculator.")
        break
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == '+':
        result = num1 + num2
        print("Result:", result)
    elif operation == '-':
        result = num1 - num2
        print("Result:", result)
    elif operation == '*':
        result = num1 * num2
        print("Result:", result)
    elif operation == '/':
        if num2 == 0:
            print("Error! Division by zero.")
        else:
            result = num1 / num2
            print("Result:", result)
    else:
        print("Invalid operation! Please enter a valid operation (+, -, *, /).")


