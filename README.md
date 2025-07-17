# Simple Desktop Reminder App

A straightforward Python script that sends continuous desktop notifications with a custom sound until manually stopped. For reminders that you absolutely cannot miss!

## ✨ Features

*   **Customizable Reminders:** Set any task you need to be reminded about.
*   **Desktop Notifications:** Utilizes your system's notification pop-ups (KDE Plasma).
*   **Audible Alerts:** Plays a custom sound with each notification.
*   **Continuous Reminders:** Keeps sending notifications at a set interval until manually stopped.
*   **Easy to Use:** Minimal setup and simple execution from the terminal.

## 🚀 Prerequisites

Before you can run this application, you need to have the following installed on your Arch Linux system:

*   **Python 3:** (Usually pre-installed or `sudo pacman -S python`).
*   **`ffmpeg`:** For converting audio files (if needed).
    ```bash
    sudo pacman -S ffmpeg
    ```
*   **`alsa-utils`:** Provides `aplay`, which is used to play the notification sound.
    ```bash
    sudo pacman -S alsa-utils
    ```
*   **`python-pip`:** Python's package installer.
    ```bash
    sudo pacman -S python-pip
    ```
*   **(Optional) `python-dbus`:** This package helps `plyer` integrate more smoothly and removes a common warning, though notifications will still work without it.
    ```bash
    sudo pacman -S python-dbus
    ```

## 🛠️ Setup Instructions

Follow these steps to get your Simple Desktop Reminder App up and running:

1.  **Navigate to your project directory:**
    Ensure you're in the `simple-reminder-app` directory (you should be if you followed the rename steps above). If not:
    ```bash
    cd ~/simple-reminder-app
    ```

2.  **Ensure your reminder script is up-to-date:**
    Make sure your `reminder.py` file contains the latest code (the one using `subprocess` for sound, and `REMINDER_INTERVAL_SECONDS = 60`). You can copy it from the last message in our conversation.

3.  **Prepare your Notification Sound:**
    This app uses `iphone_ping.wav` as the notification sound.
    *   If you downloaded an MP4 version, convert it to WAV:
        ```bash
        # Assuming your MP4 is in your Downloads folder
        ffmpeg -i "~/Downloads/"sound.mp4"" iphone_ping.wav
        ```
    *   Make sure the `iphone_ping.wav` file is located directly inside the `~/simple-reminder-app/` directory, next to `reminder.py`.

4.  **Create a Python Virtual Environment:**
    It's best practice to install Python packages in an isolated environment.
    ```bash
    python -m venv venv
    ```

5.  **Activate the Virtual Environment:**
    You'll need to do this every time you want to run the script.
    ```bash
    source venv/bin/activate
    ```
    Your terminal prompt should change to show `(venv)` at the beginning, indicating the environment is active.

6.  **Install Python Dependencies:**
    Install the necessary Python libraries using `pip` within your active virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

Once setup is complete and your virtual environment is active:

1.  **Run the application:**
    ```bash
    python reminder.py
    ```
2.  **Enter your reminder task** when prompted (e.g., "Take out the trash", "Drink water").
3.  The script will then start sending desktop notifications with sound every 60 seconds.
4.  **To stop the reminder:** Go to the terminal window where the script is running and press `Ctrl + C`.

## ⚙️ Customization

You can easily customize the reminder's behavior by editing the `reminder.py` file.

*   **`REMINDER_INTERVAL_SECONDS`**: Change the number (e.g., to `300` for 5 minutes, `120` for 2 minutes).
*   **`NOTIFICATION_TITLE`**: Modify the title of the pop-up notification.
*   **`APP_NAME`**: Change the name that appears in your notification history or settings.
*   **`SOUND_FILE_PATH`**: If you want to use a different `.wav` file, update this path. Make sure the new `.wav` file is in the `simple-reminder-app` directory or provide its full path.

## ⚠️ Troubleshooting

*   **"ModuleNotFoundError: No module named 'plyer'":**
    Ensure your virtual environment is active (`(venv)` in prompt) and you've run `pip install -r requirements.txt`.
*   **No sound:**
    *   Verify `aplay` is installed (`sudo pacman -S alsa-utils`).
    *   Confirm `iphone_ping.wav` is in the `simple-reminder-app` directory and is a valid WAV file (`aplay iphone_ping.wav` should play it).
*   **"UserWarning: The Python dbus package is not installed.":**
    This is just a warning, notifications should still work. To remove it, install `python-dbus` system-wide: `sudo pacman -S python-dbus` (deactivate venv first, then reactivate).

---
