def calculator():
    def add(a,b):
        return(a + b)
    def subtract(a,b):
        return(a - b)
    def multiply(a,b):
        return(a * b)
    def divide(a,b):
        return(a / b)

    print('Symbols ; ADD = + , SUB = -, MULTIPLY = * , DIVIDE = /')
    c = input("Enter Symbol: ")
    a = int(input("Enter First Number: "))
    b = int(input("Enter Second Number: "))
    if c == "+":
        print(add(a,b))
    elif c == "-":
        print(subtract(a,b))
    elif c == "*":
        print(multiply(a,b))
    elif c == "/":
        print(divide(a,b))
    else:
        print('Invalid Input')
calculator()