# Hello World GUI project

import tkinter as tk

root = tk.Tk()
root.title("Hello World")
root.geometry("400x250")

label = tk.Label(root, text="Hello, World!", font=("Arial", 20))
label.pack(pady=50)

button = tk.Button(root, text="Click Me", command=lambda: label.config(text="Hello, World!"))
button.pack()

root.mainloop()
