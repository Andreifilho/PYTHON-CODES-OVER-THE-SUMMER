def calculate(number1, number2, operator):
    result = 0
    if operator == "+":
        result = number1 + number2
        print(result)
    elif operator == "-":
        result = number1 - number2
        print(result)
    
    elif operator == "*":
        result = number1 * number2
        print(result)
    
    elif operator == "/":
        result = number1 / number2
        print(result)
    
calculate(10, 5, "+")  # should return 15
calculate(10, 5, "-")  # should return 5
calculate(10, 5, "*")  # should return 50
calculate(10, 5, "/")  # should return 2.0