import tkinter as tk

# Initialization
root = tk.Tk()
root.geometry("300x600")

calcStageOptions = ('selNum1', 'selOper', 'selNum2')
calcStage = calcStageOptions[0]
num1 = 0
num2 = 0
oper = 0
operSymbols = (' + ', ' - ', ' x ', ' / ')

# Callback Functions
def setNumber(number):
    global calcStage
    if calcStage == calcStageOptions[0]:
        global num1
        num1 = number
        label.config(text=str(num1))


    elif calcStage == calcStageOptions[2]:
        print("num2 is: " + str(number))
        global num2
        num2 = number
        label.config(text=str(num1) + operSymbols[oper] + str(num2))
        triggerCalculation()

    else:
        return

def setOperator(index):

    global oper, calcStage, operSymbols
    oper = index
    label.config(text=str(num1) + operSymbols[index])
    calcStage = calcStageOptions[2]

def triggerCalculation():
    global num1, num2, oper
    calc = None
    if oper == 0:
        calc = (num1 + num2)
    elif oper == 1:
        calc = (num1 - num2)
    elif oper == 2:
        calc = (num1 * num2)
    elif oper == 3:
        calc = (num1 / num2)
    else: 
        return
    
    label.config(text=str(num1) + operSymbols[oper] + str(num2) + " = " + str(calc))
    global calcStage
    calcStage = 'selNum1'
    
# GUI Setup
label = tk.Label(root, text="")
label.pack()

i = 0
while(i < 10):        
    b = tk.Button(root, 
                  text=str(i), 
                  command=lambda index=i: setNumber(index))
    b.pack()
    i += 1

j = 0
while(j < 4):
    b = tk.Button(root, 
                  text=str(operSymbols[j]), 
                  command=lambda operator=j: setOperator(operator))
    b.pack()
    j += 1

root.mainloop()