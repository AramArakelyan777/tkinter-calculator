from tkinter import Tk, Button, Entry, StringVar, messagebox

root = Tk()
root.title("Calculator")
root.geometry("337x148")
root.resizable(False, False)

expression = ""
equation = StringVar()
entry = Entry(root, textvariable=equation)


def print_command(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def clear():
    global expression
    expression = ""
    equation.set("")


def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except ZeroDivisionError:
        expression = ""
        messagebox.showerror("Error", "Can't divide by zero.")
    except Exception as exc:
        expression = ""
        messagebox.showerror("Error", f"{exc}")


entry.grid(columnspan=4, ipadx=70)

one = Button(root, text="1", bg="#F6DF42",
             command=lambda: print_command(1), height=1, width=7)
one.grid(row=2, column=0)

two = Button(root, text="2", bg="#F6DF42",
             command=lambda: print_command(2), height=1, width=7)
two.grid(row=2, column=1)

three = Button(root, text="3", bg="#F6DF42",
               command=lambda: print_command(3), height=1, width=7)
three.grid(row=2, column=2)

four = Button(root, text="4", bg="#F6DF42",
              command=lambda: print_command(4), height=1, width=7)
four.grid(row=3, column=0)

five = Button(root, text="5", bg="#F6DF42",
              command=lambda: print_command(5), height=1, width=7)
five.grid(row=3, column=1)

six = Button(root, text="6", bg="#F6DF42",
             command=lambda: print_command(6), height=1, width=7)
six.grid(row=3, column=2)

seven = Button(root, text="7", bg="#F6DF42",
               command=lambda: print_command(7), height=1, width=7)
seven.grid(row=4, column=0)

eight = Button(root, text="8", bg="#F6DF42",
               command=lambda: print_command(8), height=1, width=7)
eight.grid(row=4, column=1)

nine = Button(root, text="9", bg="#F6DF42",
              command=lambda: print_command(9), height=1, width=7)
nine.grid(row=4, column=2)

zero = Button(root, text="0", bg="#F6DF42",
              command=lambda: print_command(0), height=1, width=7)
zero.grid(row=5, column=1)

plus = Button(root, text="+", bg="#F6DF42",
              command=lambda: print_command("+"), height=1, width=7)
plus.grid(row=2, column=3)

minus = Button(root, text="-", bg="#F6DF42",
               command=lambda: print_command("-"), height=1, width=7)
minus.grid(row=3, column=3)

multiply = Button(root, text="*", bg="#F6DF42",
                  command=lambda: print_command("*"), height=1, width=7)
multiply.grid(row=4, column=3)

divide = Button(root, text="/", bg="#F6DF42",
                command=lambda: print_command("/"), height=1, width=7)
divide.grid(row=5, column=3)

equals = Button(root, text="=", bg="#F6DF42", command=equal, height=1, width=7)
equals.grid(row=5, column=2)

c = Button(root, text="C", bg="#F6DF42", command=clear, height=1, width=7)
c.grid(row=5, column=0)

root.mainloop()
