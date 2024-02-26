import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time

def set_reminder():
    message = message_entry.get()
    try:
        reminder_time = time.strptime(time_entry.get(), "%H:%M")
        current_time = time.localtime()
        reminder_time = time.struct_time((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                          reminder_time.tm_hour, reminder_time.tm_min, 0, -1, -1, -1))

        time_difference = time.mktime(reminder_time) - time.mktime(current_time)
        if time_difference <= 0:
            messagebox.showerror("Error", "Invalid Time!")
            return

        time.sleep(time_difference)
        notification.notify(
            title="Reminder",
            message=message,
            timeout=10
        )
    except ValueError:
        messagebox.showerror("Error", "Invalid Time Format!")

# GUI setup
root = tk.Tk()
root.title("Reminder Application")

message_label = tk.Label(root, text="Enter your reminder message:")
message_label.pack()
message_entry = tk.Entry(root, width=50)
message_entry.pack()

time_label = tk.Label(root, text="Enter reminder time (HH:MM):")
time_label.pack()
time_entry = tk.Entry(root, width=50)
time_entry.pack()

set_button = tk.Button(root, text="Set Reminder", command=set_reminder)
set_button.pack()

root.mainloop()
