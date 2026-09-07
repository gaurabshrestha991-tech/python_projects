#   GUI Digital Clock using Tkinter

import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(1000, update_clock)
    
window = tk.Tk()
window.title("Digital Clock")
window.geometry("400x150")

clock = tk.Label(window, font=("Arial", 50))
clock.pack(expand=True)

update_clock()
window.mainloop()