def addNumbers(num1, num2):
    return num1 + num2

def substractNumbers(num1, num2):
    return num1 - num2

def multiplyNumbers(num1, num2):
    return num1*num2

def divideNumbers(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("You can't divide by zero.")