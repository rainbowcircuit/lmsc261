# Prompt User Input
num1 = input("Enter Number 1: ")
oper = input("Select Operation: ") # Type +, -, *, or /
num2 = input("Enter Number 2: ")

# Define the calculation function
def calculate():
    # print(num1 + num2) will result in string concatnation: 4 + 2 = 42
    # float(num1) ensures that num1 and num2 are treated as numbers.

    if oper == "+":
        print(float(num1) + float(num2)) 

    elif oper == "-":
        print(float(num1) - float(num2))

    elif oper == "*":
        print(float(num1) * float(num2))

    elif oper == "/":
        print(float(num1) * float(num2))

    else:
        # If the user types anything else, print an error message, and return.
        print("Invalid Operation")
        return

# Trigger Calculation
calculate()