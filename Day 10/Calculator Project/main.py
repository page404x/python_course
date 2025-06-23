from art import logo

def add(n1, n2):
    """Simple mathematical function to add 2 given numbers"""
    return n1 + n2

def subtract(n1, n2):
    """A simple mathematical function to subtract 2 given numbers"""
    return n1 - n2

def multiply(n1, n2):
    """a simple mathematical function to multiply 2 given numbers"""
    return n1 * n2

def divide(n1, n2):
    """a simple mathematical function to dived 2 given numbers"""
    return n1 / n2

math_func = {"+":add, "-" :subtract, "*" : multiply, "/": divide}

repeat = True
while repeat:
    print(logo)
    x = int(input("What is your first number: "))
    y = int(input("What is your second number: "))
    operator_symbol = input("Type a mathematical operator : ")
    print(f"Mathematical result is : {math_func[operator_symbol](x,y)}")
    ask = input("Do you want to calculate more? ").lower()
    if ask == 'y':
        repeat = True
    else:
        repeat = False

