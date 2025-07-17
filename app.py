import time
import threading
import subprocess
import sys # For detecting OS for sound playback
import os # For checking if sound file exists

from plyer import notification
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Global Variables for Reminder State ---
stop_event = threading.Event() # Signals the reminder thread to stop
reminder_thread = None         # Holds the reminder thread
current_task = None            # Stores the current task
current_interval = None        # Stores the current interval

# --- Configuration ---
NOTIFICATION_TITLE = "Reminder!"
APP_NAME = "My Reminder"
SOUND_FILE_PATH = "iphone_ping.wav" # Ensure this .wav file is in the same directory as app.py

# --- Function to play sound based on OS ---
def play_sound(sound_file):
    try:
        # Check if sound file exists (cross-platform way)
        if not os.path.exists(sound_file):
            print(f"Warning: Sound file not found at {sound_file}. Sound will not play.")
            return

        if sys.platform.startswith('linux'):
            # Linux: Uses aplay (from alsa-utils)
            subprocess.run(['aplay', sound_file], check=True, capture_output=True, text=True)
        elif sys.platform.startswith('darwin'):
            # macOS: Uses afplay (built-in)
            subprocess.run(['afplay', sound_file], check=True, capture_output=True, text=True)
        elif sys.platform.startswith('win'):
            # Windows: Uses PowerShell to play sound
            powershell_command = f"(New-Object Media.SoundPlayer '{sound_file}').PlaySync();"
            subprocess.run(['powershell', '-command', powershell_command], check=True, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
        else:
            print(f"Warning: Unsupported OS ({sys.platform}) for direct sound playback. Sound will not play.")
    except FileNotFoundError as e:
        print(f"Warning: Command not found for sound playback on your OS ({sys.platform}): {e}. Sound will not play.")
        print("Please ensure native audio tools are installed (e.g., alsa-utils on Linux).")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to play sound. Error (stderr): {e.stderr.strip()}. Sound will not play.")
    except Exception as e:
        print(f"Warning: An unexpected error occurred during sound playback: {e}. Sound will not play.")

# --- Function to run in a separate thread for continuous notifications ---
def run_reminder_loop(task, interval_seconds, stop_event_obj):
    global current_task, current_interval
    current_task = task
    current_interval = interval_seconds
    print(f"Reminder thread started for '{task}' every {interval_seconds}s.")

    while not stop_event_obj.is_set(): # Loop until the stop event is set
        # Send desktop notification
        notification.notify(
            title=NOTIFICATION_TITLE,
            message=f"Task: {task}",
            app_name=APP_NAME,
            timeout=10 # Notification stays for 10 seconds
        )
        
        # Play sound using OS-specific method
        play_sound(SOUND_FILE_PATH)

        print(f"Notification sent: '{task}'")
        
        # Wait for the next interval, but check stop_event periodically
        stop_event_obj.wait(interval_seconds) 
    
    current_task = None # Clear task when stopped
    current_interval = None
    print("Reminder thread stopped.")

# --- Flask Web Application Routes ---

@app.route('/')
def index():
    # Display the main reminder page
    return render_template('index.html', 
                           is_active=reminder_thread and reminder_thread.is_alive(),
                           task=current_task,
                           interval=current_interval)

@app.route('/start', methods=['POST'])
def start_reminder():
    global reminder_thread, stop_event

    task = request.form['task'].strip()
    try:
        interval_seconds = int(request.form['interval'])
        if interval_seconds < 5: # Minimum interval of 5 seconds
            interval_seconds = 5
    except ValueError:
        return "Invalid interval. Must be a number.", 400

    if not task:
        return "Task cannot be empty.", 400

    # If a reminder is already running, stop it first
    if reminder_thread and reminder_thread.is_alive():
        stop_event.set() # Signal the old thread to stop
        reminder_thread.join(timeout=2) # Wait a bit for it to stop
        
    # Reset stop signal and start new thread
    stop_event.clear()
    reminder_thread = threading.Thread(target=run_reminder_loop, args=(task, interval_seconds, stop_event))
    reminder_thread.daemon = True # Thread exits when main app exits
    reminder_thread.start()

    return redirect(url_for('index')) # Go back to the main page

@app.route('/stop', methods=['POST'])
def stop_reminder():
    global reminder_thread, stop_event
    if reminder_thread and reminder_thread.is_alive():
        stop_event.set() # Signal the thread to stop
        reminder_thread.join(timeout=2) # Wait a bit for it to stop
    return redirect(url_for('index')) # Go back to the main page

# Run the Flask web application
if __name__ == '__main__':
    app.run(debug=False, host='127.0.0.1', port=5000)