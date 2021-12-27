import tkinter
from typing import Text

window = tkinter.Tk()

window.title("Welcome")
window.minsize(width=500, height=500)

label = tkinter.Label(text="Button Clicked : ", font=("Arial", 24, "bold"))
label.pack()

label1 = tkinter.Label(text="", font=("Arial", 24, "bold"))
label1.pack()

count = 0
def button_clicked():
    global count
    count += 1
    label1['text'] = count
    print(input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

input = tkinter.Entry(width=50)
input.pack()



window.mainloop()