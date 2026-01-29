import tkinter as tk

root = tk.Tk()
root.geometry("400x400")

operOptions = ('+', '-', 'x', '/')

def numButtonPressed(index):
    print("Button Pressed! " + str(index))

def operButtonPressed(index):
    print("Operator Pressed! " + operOptions[index])

# set up number buttons
numButtonIndex = 0
while numButtonIndex < 10:
    numButton = tk.Button(text=str(numButtonIndex), 
                        command=lambda index=numButtonIndex: numButtonPressed(index))
    numButton.pack()
    numButtonIndex += 1

# set up operator buttons
operButtonIndex = 0
while operButtonIndex < 4:
    operButton = tk.Button(text=operOptions[operButtonIndex], 
                        command=lambda index=operButtonIndex: operButtonPressed(index))
    operButton.pack()
    operButtonIndex += 1

root.mainloop()