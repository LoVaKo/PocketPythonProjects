'''
This is a simple calculator. To add more operations:
- add the operator to the list of operators.
- define the function
- add the combination to the match statement in calculate()
'''

operators = ["+", "-", "*", "/"]

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def times(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def pick_operator():
    while True:
        user_input = input(f"Please choose one of the following operations {operators}:")
        
        if user_input in operators: 
            return user_input
        
        print("Invalid operator.")


def pick_number(nth):
    while True:
        try:
            user_input = int(input(f"Please enter the {nth} number: "))

            #  The following block checks for a possible zero division error.
            if nth != "second": 
                return user_input
            if operation != "/":
                return user_input
            if user_input != 0:
                return user_input
            print("You cannot divide by zero. Please choose a different number.")

        except ValueError:
            print("Invalid input. Please enter an integer.")


def calculate(operator, num1, num2):
    match operator:
        case "+": return add(num1, num2)
        case "-": return subtract(num1, num2)
        case "*": return times(num1, num2)
        case "/": return divide(num1, num2)


while True:            
    operation = pick_operator()
    number_1 = pick_number("first")
    number_2 = pick_number("second")
    result = calculate(operation, number_1, number_2)

    print(f"{number_1} {operation} {number_2} = {result}")

    proceed = input("Would you like to proceed?[Y/n]: ").lower()
    if proceed == "n": 
        break

