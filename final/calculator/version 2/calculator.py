# initializing variables 
num1 = None
num2 = None
isSettingNum1 = True
oper = None
operOptions = ('+', '-', 'x', '/')

# defining functions
def setNumber(number):
    global num1, num2, calcStage
    if isSettingNum1:
        num1 = int(number)
    else:
        num2 = int(number)

def setOperator(operator):
    global oper
    oper = operator

def calculateNumbers(a, b):
    if oper == operOptions[0]:
        print(a + b)
    elif oper == operOptions[1]:
        print(a - b)
    elif oper == operOptions[2]:
        print(a * b)
    elif oper == operOptions[3]:
        print(a / b)
    else:
        print('uh oh')


# running the program
setNumber(input("Set first number: "))
setOperator(input("Set operator: "))
isSettingNum1 = False
setNumber(input("Set second number: "))

calculateNumbers(num1, num2)