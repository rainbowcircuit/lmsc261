# initializing variables 
num1 = None
num2 = None
isSettingNum1 = True

# defining functions
def setNumber(number):
    global num1, num2, calcStage
    if isSettingNum1:
        num1 = int(number)
    else:
        num2 = int(number)

def addNumbers(a, b):
    print(a + b)

# running the program
setNumber(input("Set first number: "))
calcStage = False
setNumber(input("Set second number: "))
addNumbers()