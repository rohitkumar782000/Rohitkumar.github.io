from tkinter import *

def click(event):
    global answer
    text = event.widget.cget("text")
    if text == "=":
        if answer.get().isdigit():
            value = int(answer.get())
        else:
            value = eval(Output_Box.get())
        answer.set(value)
        Output_Box.update()

    elif text == "C":
        answer.set("")
        Output_Box.update()
    else:
        answer.set(answer.get() + text)
        Output_Box.update()


root = Tk()
root.geometry("410x625")
root.title("Personal Calculator")
# root.wm_iconbitmap("cal.ico")
root.config(bg="black")

f1 = Frame(root).pack()
answer = StringVar()
answer.set("")

Output_Box = Entry(f1, textvariable=answer, font=("lucida", 40 , "bold"))
Output_Box.pack(fill=X,  ipadx=8, pady=10, padx=10)

keys = Frame(root)
keys.pack()

btn_clear = Button(keys, text="C", font=("Fira Sans", 32), bg="black", fg="white")
btn_clear.grid(row=0, column=0, padx=8, pady=8)
btn_clear.bind("<Button-1>", click)

btn_percent = Button(keys, text="%", font=("Fira Sans", 32), bg="black", fg="white")
btn_percent.grid(row=0, column=1, padx=8, pady=8)
btn_percent.bind("<Button-1>", click)

btn_erease = Button(keys, text="<", font=("Fira Sans", 32), bg="black", fg="white")
btn_erease.grid(row=0, column=2, padx=8, pady=8)
btn_erease.bind("<Button-1>", click)

btn_divide = Button(keys, text="/", font=("Fira Sans", 32), width=3, bg="black", fg="white")
btn_divide.grid(row=0, column=3, padx=8, pady=8)
btn_divide.bind("<Button-1>", click)

btn_7 = Button(keys, text="7", font=("Fira Sans", 32), bg="black", fg="white")
btn_7.grid(row=1, column=0, padx=8, pady=8)
btn_7.bind("<Button-1>", click)

btn_8 = Button(keys, text="8", font=("Fira Sans", 32), bg="black", fg="white")
btn_8.grid(row=1, column=1, padx=8, pady=8)
btn_8.bind("<Button-1>", click)

btn_9 = Button(keys, text="9", font=("Fira Sans", 32), bg="black", fg="white")
btn_9.grid(row=1, column=2, padx=8, pady=8)
btn_9.bind("<Button-1>", click)

btn_multfly = Button(keys, text="*", font=("Fira Sans", 32), width=3, bg="black", fg="white")
btn_multfly.grid(row=1, column=3, padx=8, pady=8)
btn_multfly.bind("<Button-1>", click)

btn_4 = Button(keys, text="4", font=("Fira Sans", 32), bg="black", fg="white")
btn_4.grid(row=2, column=0, padx=8, pady=8)
btn_4.bind("<Button-1>", click)

btn_5 = Button(keys, text="5", font=("Fira Sans", 32), bg="black", fg="white")
btn_5.grid(row=2, column=1, padx=8, pady=8)
btn_5.bind("<Button-1>", click)

btn_6 = Button(keys, text="6", font=("Fira Sans", 32), bg="black", fg="white")
btn_6.grid(row=2, column=2, padx=8, pady=8)
btn_6.bind("<Button-1>", click)

btn_subtract = Button(keys, text="-", font=("Fira Sans", 32), width=3, bg="black", fg="white")
btn_subtract.grid(row=2, column=3, padx=8, pady=8)
btn_subtract.bind("<Button-1>", click)

btn_1 = Button(keys, text="1", font=("Fira Sans", 32), bg="black", fg="white")
btn_1.grid(row=3, column=0, padx=8, pady=8)
btn_1.bind("<Button-1>", click)

btn_2 = Button(keys, text="2", font=("Fira Sans", 32), bg="black", fg="white")
btn_2.grid(row=3, column=1, padx=8, pady=8)
btn_2.bind("<Button-1>", click)

btn_3 = Button(keys, text="3", font=("Fira Sans", 32), bg="black", fg="white")
btn_3.grid(row=3, column=2, padx=8, pady=8)
btn_3.bind("<Button-1>", click)

btn_add = Button(keys, text="+", font=("Fira Sans", 32), width=3, bg="black", fg="white")
btn_add.grid(row=3, column=3, padx=8, pady=8)
btn_add.bind("<Button-1>", click)

btn_dot = Button(keys, text=".", font=("Fira Sans", 32), bg="black", fg="white")
btn_dot.grid(row=4, column=0, padx=8, pady=8)
btn_dot.bind("<Button-1>", click)

btn_0 = Button(keys, text="", font=("Fira Sans", 32), bg="black", fg="white")
btn_0.grid(row=4, column=1, padx=8, pady=8)
btn_0.bind("<Button-1>", click)

btn_00 = Button(keys, text="00", font=("Fira Sans", 32), bg="black", fg="white")
btn_00.grid(row=4, column=2, padx=8, pady=8)
btn_00.bind("<Button-1>", click)

btn_equal = Button(keys, text="=", font=("Fira Sans", 32), width=3, bg="black", fg="white")
btn_equal.grid(row=4, column=3, padx=8, pady=8)
btn_equal.bind("<Button-1>", click)


root.mainloop()
