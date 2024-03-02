import tkinter as tk

def button_click(symbol):
    current = entry_display.get()
    entry_display.delete(0, tk.END)
    entry_display.insert(tk.END, current + str(symbol))

def clear_display():
    entry_display.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry_display.get())
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, result)
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry_display = tk.Entry(root, width=35, borderwidth=5)
entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_num = 1
col_num = 0

for button in buttons:
    if col_num > 3:
        col_num = 0
        row_num += 1

    if button == '=':
        tk.Button(root, text=button, padx=40, pady=20, command=calculate).grid(row=row_num, column=col_num, columnspan=2)
        col_num += 1
    elif button == '0':
        tk.Button(root, text=button, padx=40, pady=20, command=lambda symbol=button: button_click(symbol)).grid(row=row_num, column=col_num, columnspan=2)
        col_num += 1
    else:
        tk.Button(root, text=button, padx=40, pady=20, command=lambda symbol=button: button_click(symbol)).grid(row=row_num, column=col_num)
    col_num += 1

tk.Button(root, text="Clear", padx=30, pady=20, command=clear_display).grid(row=row_num, column=3)

root.mainloop()
