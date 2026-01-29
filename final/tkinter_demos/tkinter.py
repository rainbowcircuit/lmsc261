from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x600")

isMyBool = 0

# Labels #
label = ttk.Label(root, text="Current Count: ");
label.pack()


def buttonCommand():
    global isMyBool
    isMyBool += 1
    print(isMyBool)
    label.config(text=str(isMyBool))
    
def getText():
    textAsString = entry.get()
    print(textAsString)

def validText():
    return True


# Buttons #
button = ttk.Button(root, text="Count", command=buttonCommand)
button.pack()

# Entry #
entry = ttk.Entry(root)
entry.pack()
entry.register(validText)

entryButton = ttk.Button(text="Get Text", command=getText)
entryButton.pack()

# Menu #

optionList = ('train', 'plane', 'boat', 'car', 'bicycle')
optionListDefault = StringVar()
optionListDefault.set(optionList[0])
optionMenu = ttk.OptionMenu(root, optionListDefault, *optionList)
optionMenu.pack()




root.mainloop()
