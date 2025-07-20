import tkinter as tk
from tkinter import messagebox
import threading
import time

from plyer import notification

# --- Global Variables ---
reminder_thread = None
stop_event = threading.Event()

# --- Core Reminder Logic ---
def play_sound():
    # This schedules the app.bell() method to be called on the main GUI thread.
    # It's the correct and safe way to trigger a system sound from a background thread in Tkinter.
    app.after(0, app.bell)

def reminder_loop(task, interval):
    print(f"Reminder thread started for '{task}' every {interval}s.")
    while not stop_event.is_set():
        notification.notify(
            title="Reminder!",
            message=f"Don't forget: {task}",
            app_name="Simple Reminder App",
            timeout=10
        )
        play_sound()
        print(f"Notification sent for: '{task}'")
        
        # Wait for the interval, but allow for a quick stop
        for _ in range(interval):
            if stop_event.is_set():
                break
            time.sleep(1)
    
    print("Reminder thread stopped.")
    app.after(0, update_gui_on_stop)

# --- GUI Functions ---
def start_button_clicked():
    global reminder_thread
    task = task_entry.get().strip()
    try:
        interval = int(interval_entry.get())
        if interval < 5:
            messagebox.showwarning("Warning", "Interval must be at least 5 seconds.")
            return
    except ValueError:
        messagebox.showwarning("Warning", "Interval must be a number.")
        return

    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty.")
        return
        
    stop_button_clicked() # Stop any previous reminder

    stop_event.clear()
    reminder_thread = threading.Thread(target=reminder_loop, args=(task, interval))
    reminder_thread.daemon = True
    reminder_thread.start()

    update_gui_on_start(task, interval)

def stop_button_clicked():
    if reminder_thread and reminder_thread.is_alive():
        stop_event.set()
        reminder_thread.join(timeout=2)

def update_gui_on_start(task, interval):
    status_label.config(text=f"ACTIVE: Reminding you about '{task}'", fg="green")
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    task_entry.config(state=tk.DISABLED)
    interval_entry.config(state=tk.DISABLED)

def update_gui_on_stop():
    status_label.config(text="No reminder running.", fg="red")
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    task_entry.config(state=tk.NORMAL)
    interval_entry.config(state=tk.NORMAL)

# --- GUI Setup ---
app = tk.Tk()
app.title("Simple Reminder")
app.geometry("400x200")
app.resizable(False, False)

main_frame = tk.Frame(app, padx=20, pady=20)
main_frame.pack()

tk.Label(main_frame, text="Task:").grid(row=0, column=0, sticky="w", pady=5)
task_entry = tk.Entry(main_frame, width=30)
task_entry.grid(row=0, column=1)
task_entry.insert(0, "Take a break")

tk.Label(main_frame, text="Interval (sec):").grid(row=1, column=0, sticky="w", pady=5)
interval_entry = tk.Entry(main_frame, width=30)
interval_entry.grid(row=1, column=1)
interval_entry.insert(0, "60")

start_button = tk.Button(main_frame, text="Start Reminder", command=start_button_clicked)
start_button.grid(row=2, column=0, pady=10)

stop_button = tk.Button(main_frame, text="Stop Reminder", command=stop_button_clicked, state=tk.DISABLED)
stop_button.grid(row=2, column=1, pady=10)

status_label = tk.Label(main_frame, text="No reminder running.", fg="red")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

def on_closing():
    stop_button_clicked()
    app.destroy()

app.protocol("WM_DELETE_WINDOW", on_closing)
app.mainloop()