import tkinter as tk

def on_button_click(value):
    current_text = entry_var.get()
    entry_var.set(current_text + value)

def clear_entry():
    entry_var.set("")

def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(result)
    except Exception as e:
        entry_var.set("Error")


root = tk.Tk()
root.title("Simple Calculator")

entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var, justify="right", font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4)


buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


row_val = 1
col_val = 0
for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 16),
              command=lambda b=button: on_button_click(b) if b != '=' else calculate_result()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

tk.Button(root, text='C', padx=20, pady=20, font=("Arial", 16), command=clear_entry).grid(row=row_val, column=col_val)

root.mainloop()
