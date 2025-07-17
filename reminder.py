import time
from plyer import notification
import subprocess # For running system commands like 'aplay'

# --- Configuration ---
REMINDER_INTERVAL_SECONDS = 10
NOTIFICATION_TITLE = "Action Required!"
APP_NAME = "Simple Reminder"

# Path to your WAV sound file. This should be correct!
SOUND_FILE_PATH = "iphone_ping.wav" 

# --- 1. Get the task from the user ---
task = input("What do you need to be reminded about? ")
print(f"Okay, I'll start sending you desktop notifications and a sound every {REMINDER_INTERVAL_SECONDS} seconds for '{task}'.")
print("This will continue until you manually stop the script (e.g., by pressing Ctrl+C in this terminal).")
print("(Keep this terminal window open for the script to run.)")

# --- 2. Start the reminder loop (no more user input within the loop) ---
while True: # Loop indefinitely
    # --- 3. Send the desktop notification ---
    notification.notify(
        title=NOTIFICATION_TITLE,
        message=f"Don't forget: {task}",
        app_name=APP_NAME,
        timeout=10 
    )
    
    # --- Play a sound using aplay via subprocess ---
    try:
        if not subprocess.run(['test', '-f', SOUND_FILE_PATH]).returncode == 0:
            print(f"Warning: Sound file not found at {SOUND_FILE_PATH}. Sound will not play.")
        else:
            subprocess.run(['aplay', SOUND_FILE_PATH], check=True, capture_output=True, text=True)
    except FileNotFoundError:
        print("Warning: 'aplay' command not found. Cannot play sound. Please ensure 'alsa-utils' is installed.")
    except subprocess.CalledProcessError as e:
        print(f"Warning: Failed to play sound with aplay. Error (stderr): {e.stderr.strip()}")
    except Exception as e:
        print(f"Warning: An unexpected error occurred while trying to play sound: {e}")

    # --- Also print to console for consistency/debugging ---
    print(f"\n--- DESKTOP REMINDER SENT (with sound!) ---")
    print(f"ACTION REQUIRED: {task}")
    print(f"-----------------------------------------")

    # --- 4. Wait for the next reminder ---
    time.sleep(REMINDER_INTERVAL_SECONDS) # Pause the program for the specified time

# This line will never be reached in the current infinite loop
# print("Reminder program finished. Goodbye!") 
