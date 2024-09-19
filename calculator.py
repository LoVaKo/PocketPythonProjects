while True:
    user_input = input("Please choose one of the following operations [+ - * /]:")
    if user_input in ["+", "-", "*", "/"]: 
        operation = user_input
        break
    else:
        print("Invalid operator.")

while True:
    try:
        number_1 = int(input("Please enter the first number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

while True: 
    try:
        number_2 = int(input("Please enter the second number: "))
        
        if operation == "/" and number_2 == 0:
            print("You cannot divide by zero. Please choose a different number.")
            continue
        
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
result = 0

match operation:
    case "+": result = number_1 + number_2
    case "-": result = number_1 - number_2
    case "*": result = number_1 * number_2
    case "/": result = number_1 / number_2

print(f"{number_1} {operation} {number_2} = {result}")



