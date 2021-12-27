import tkinter

window = tkinter.Tk()

window.title("Welcome")
window.minsize(width=200, height=100)

miles_input = tkinter.Entry()
miles_input.grid(column=1, row=0)

lbl1 = tkinter.Label(text="is equal to ", font=("Arial", 14, "bold"))
lbl1.grid(column=0, row=1)

lbl2 = tkinter.Label(text="0")
lbl2.grid(column=1, row=1)

lbl3 = tkinter.Label(text="Km")
lbl3.grid(column=2, row=1)

def mileconv():
    mile = float(miles_input.get())
    km = mile * 1.609
    lbl2.config(text=f"{km}")

btnCalc = tkinter.Button(text="Calculate", command=mileconv)    
btnCalc.grid(column=1, row=2)



window.mainloop()