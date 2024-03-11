import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def calculate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = result
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
    except (SyntaxError, ZeroDivisionError, NameError):
        clear()
        text_result.insert(1.0, "Error: Invalid Expression")

def clear():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

root = tk.Tk()
root.geometry("400x300")
text_result = tk.Text(root, height=4, width=18, font=("Arial", 24))
text_result.grid(columnspan=8)


for i in range(11):
    btn = tk.Button(root, text=str(i), command=lambda i=i: add_to_calculation(i), width=6, font=("Arial", 14))
    btn.grid(row=3 + (i-1) // 3, column=(i-1) % 3 + 1)


btn_add = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=6, font=("Arial", 14))
btn_add.grid(row=2, column=1)

btn_subtract = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=6, font=("Arial", 14))
btn_subtract.grid(row=2, column=2)

btn_multiply = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=6, font=("Arial", 14))
btn_multiply.grid(row=2, column=3)

btn_divide = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=6, font=("Arial", 14))
btn_divide.grid(row=2, column=4)

btn_clear = tk.Button(root, text="C", command=clear, width=6, font=("Arial", 14))
btn_clear.grid(row=3, column=4)

btn_equal = tk.Button(root, text="=", command=calculate, width=6, font=("Arial", 14))
btn_equal.grid(row=4, column=4)

root.mainloop()
