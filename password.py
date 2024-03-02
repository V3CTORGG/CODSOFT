import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    length = int(entry_length.get())
    if length <= 0:
        result_label.config(text="Please enter a valid length")
        return
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    result_label.config(text=password)

root = tk.Tk()
root.title("Password Generator")

main_frame = ttk.Frame(root, padding="20")
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
main_frame.columnconfigure(0, weight=1)
main_frame.rowconfigure(0, weight=1)

label_length = ttk.Label(main_frame, text="Password Length:")
label_length.grid(column=0, row=0, sticky=tk.W)

entry_length = ttk.Entry(main_frame, width=10)
entry_length.grid(column=1, row=0, sticky=tk.W)

generate_button = ttk.Button(main_frame, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=1, columnspan=2, pady=10)

result_label = ttk.Label(main_frame, text="", wraplength=300)
result_label.grid(column=0, row=2, columnspan=2)

root.mainloop()
