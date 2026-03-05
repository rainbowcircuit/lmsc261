import tkinter as tk

root = tk.Tk();
root.geometry("200x200")

canvas = tk.Canvas(root, bg="#ffffff", width="100", height="200");
canvas.pack()

def sliderMoved(sliderPosition):
    print(sliderPosition)

slider = tk.Scale(root, command=sliderMoved, orient="horizontal", background="#ffffff")
slider.pack()


root.mainloop()