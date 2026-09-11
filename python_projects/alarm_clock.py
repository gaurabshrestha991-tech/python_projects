import tkinter as tk
from datetime import datetime
import os

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x300")

alarm_time = ""

def set_alarm():
    global alarm_time
    alarm_time = time_entry.get()
    status.config(text= "Alarm set for" + alarm_time)
    
def check_alarm():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock.config(text=current_time)
    
    if alarm_time == current_time[:5]:
        status.config(text="ALARM!")
        
        os.system("paplay /usr/share/sounds/freedesktop/stereo/alarm-clock-elapsed.oga")
        
    root.after(1000, check_alarm)

clock = tk.Label(root, font=("Arial", 40))
clock.pack(pady=30)

time_entry = tk.Entry(root, font=("Arial", 20), justify="center")
time_entry.pack()

time_entry.insert(0, "HH:MM")

set_button = tk.Button(
    root,
    text="Set Alarm",
    font=("Arial", 15),
    command=set_alarm
)
set_button.pack(pady=15)

status = tk.Label(root, text="No alarm set", font=("Arial",14))
status.pack()

check_alarm()
root.mainloop()