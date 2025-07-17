# Simple Desktop Reminder App ⏰

A minimalist, web-interface reminder application designed to send persistent desktop notifications with an audible alert until manually dismissed. Works across Linux, Windows, and macOS.

## ✨ Features

*   **Cross-Platform Compatibility:** Runs seamlessly on Linux, Windows, and macOS.
*   **Web-based Interface:** Easily set and manage reminders from your web browser.
*   **Customizable Reminders:** Set any task and custom interval.
*   **Desktop Pop-up Notifications:** Leverages your operating system's native notification system for visual alerts.
*   **Audible Alerts:** Plays a distinct sound (`iphone_ping.wav`) with each notification to ensure you don't miss it.
*   **Continuous Reminders:** Keeps sending notifications at a set interval until manually stopped via the web interface.
*   **Very Simple:** Minimal code and clear interaction via a local web page.

---

## ⚠️ Important User Information

### Local Desktop Application

This application runs directly on your local machine. It is **not a remote web service** and cannot be accessed from outside your local network (unless specifically configured for that, which is not covered here). It interacts with your local desktop environment for notifications and sound.

### Terminal Dependency

For the reminder to function, the terminal window (or Command Prompt/PowerShell on Windows, Terminal on macOS) where the `python app.py` command is executed **must remain open**. Closing this terminal will stop both the web server and the reminder process.

---

## 🛠️ How It Works (Tech Stack)

This project combines Python web capabilities with direct system interaction to provide a robust, cross-platform reminder experience.

*   **Python 3:** The core programming language.
*   **Flask:** A lightweight Python web framework for handling the web interface.
*   **`plyer`:** A cross-platform Python library used to send desktop notifications to your OS.
*   **`subprocess` module:** Python's standard library for running external commands (used for playing sounds via native tools).
*   **Platform-Specific Audio Tools:**
    *   **Linux:** `aplay` (from `alsa-utils`)
    *   **macOS:** `afplay` (built-in)
    *   **Windows:** PowerShell's `SoundPlayer` (.NET class)
*   **HTML/CSS:** Structures and styles the web interface.
*   **Python Virtual Environments:** Ensures project dependencies are isolated and managed cleanly.

---

## 🚀 Getting Started (Setup & Usage)

To set up and run this project on your machine, follow the instructions for your specific operating system.

### All Operating Systems (Common Steps)

1.  **Clone this repository (if you're starting fresh from GitHub):**
    ```bash
    git clone https://github.com/your_username/simple-reminder-app.git # Replace your_username
    cd simple-reminder-app
    ```
    *If you've been following along, your project folder is already set up; just `cd ~/simple-reminder-app` to enter it.*

2.  **Prepare your Notification Sound:**
    The app uses `iphone_ping.wav` as the default notification sound.
    *   If you have the original MP4 version, convert it to WAV and ensure it's in the project's root directory (`~/simple-reminder-app/`):
        ```bash
        # Example conversion using ffmpeg (install ffmpeg if you don't have it)
        # Ensure your current directory in terminal is where the MP4 is located before running ffmpeg.
        # Then, ensure 'iphone_ping.wav' is moved/copied to your project root.
        ffmpeg -i "path/to/IPHONE NOTIFICATION SOUND EFFECT (PING／DING).mp4" iphone_ping.wav
        ```
    *   Verify `iphone_ping.wav` is located directly inside the `~/simple-reminder-app/` directory (next to `app.py`).

3.  **Create a Python Virtual Environment:**
    ```bash
    python -m venv venv
    ```

4.  **Activate the Virtual Environment:**
    *   **Linux/macOS:**
        ```bash
        source venv/bin/activate
        ```
    *   **Windows (Command Prompt):**
        ```cmd
        venv\Scripts\activate.bat
        ```
    *   **Windows (PowerShell):**
        ```powershell
        .\venv\Scripts\Activate.ps1
        ```
    Your terminal prompt should change to show `(venv)` at the beginning, indicating the environment is active.

5.  **Install Python Dependencies:**
    This installs `Flask` and `plyer` (your web framework and notification library).
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1.  **Start the web application (after common setup and venv activation):**
    ```bash
    python app.py
    ```
    You will see messages in your terminal indicating that the Flask server is running, typically on `http://127.0.0.1:5000`.

2.  **Open your web browser** and navigate to the address provided by the Flask server (e.g., `http://127.0.0.1:5000`).

3.  **Use the web interface:**
    *   Enter your reminder task and the desired interval (in seconds).
    *   Click "Start Reminder". Notifications and sounds will begin.
    *   To stop an active reminder, click "Stop Reminder" on the web page.

4.  **To stop the web server:** Go to the terminal window where `python app.py` is running and press `Ctrl + C`.

### Operating System Specific Prerequisites

Beyond the common steps, ensure you have these system-level tools installed based on your OS:

*   **Linux (e.g., Arch Linux KDE):**
    ```bash
    sudo pacman -S python       # Python 3
    sudo pacman -S ffmpeg       # For converting audio files (if needed)
    sudo pacman -S alsa-utils   # Provides 'aplay' for sound playback
    sudo pacman -S python-pip   # Python's package installer
    # sudo pacman -S python-dbus  # Optional: For better plyer integration, removes warning
    ```

*   **Windows:**
    *   **Python 3:** Download and install from [python.org](https://www.python.org/downloads/windows/). Crucially, check "Add Python to PATH" during installation.
    *   **ffmpeg:** Download from [ffmpeg.org](https://ffmpeg.org/download.html). Extract it and consider adding its `bin` directory to your system's PATH if you plan to use it for conversion.
    *   PowerShell is built-in and handles sound playback.

*   **macOS:**
    *   **Python 3:** (Often pre-installed or install via Homebrew: `brew install python`).
    *   **ffmpeg:** (Install via Homebrew: `brew install ffmpeg`)
    *   `afplay` is built-in and handles sound playback. You may need to grant notification permissions for the Terminal app or Python itself.

---

## ⚙️ Customization (Source Code)

You can easily tailor the reminder's behavior by editing the `app.py` file in a text editor like VSCodium.

*   **`REMINDER_INTERVAL_SECONDS`**: Change the default number of seconds in the web form's input.
*   **`NOTIFICATION_TITLE`**: Modify the bold title that appears on the pop-up notification.
*   **`APP_NAME`**: Change the application name that might appear in your system's notification history.
*   **`SOUND_FILE_PATH`**: To use a different `.wav` sound, update this path. Make sure the new `.wav` file is placed in the `simple-reminder-app` directory or provide its full system path.
*   **`app.run(port=5000)`**: Change `port=5000` to a different number if port 5000 is already in use on your system.

---

## ⚠️ Troubleshooting

*   **"Address already in use" (Flask server error):**
    *   Another program is using port 5000 (or the port you configured).
    *   Find the process using the port (e.g., `sudo ss -tulnp | grep 5000` on Linux) and kill it (`sudo kill PID`).
    *   Alternatively, change the `port=` number in `app.run()` within `app.py` and restart.
*   **"ModuleNotFoundError: No module named 'Flask'" or 'plyer':**
    *   Ensure your virtual environment is active (`(venv)` in your terminal prompt).
    *   Run `pip install -r requirements.txt` again while the virtual environment is active.
*   **No desktop notifications (but script runs):**
    *   Check your OS notification settings (e.g., "Focus Assist" on Windows, "Do Not Disturb" modes on any OS).
    *   On macOS, you might need to manually grant notification permissions for the Terminal app or Python.
    *   On Linux, consider installing `python-dbus` (`sudo pacman -S python-dbus`) to improve `plyer` integration.
*   **No sound despite reminder active:**
    *   Confirm `iphone_ping.wav` exists in the project directory and is a valid WAV file.
    *   Check the `SOUND_FILE_PATH` in `app.py` is correct.
    *   **Linux:** Verify `aplay` is installed (`sudo pacman -S alsa-utils`).
    *   **Windows:** Ensure PowerShell is working correctly.
    *   **macOS:** Ensure `afplay` is available (usually built-in).
    *   Check your system's volume and audio output settings.
*   **"FileNotFoundError: [Errno 2] No such file or directory: 'aplay' / 'afplay' / 'powershell'":**
    This means the required command-line audio tool is not found in your system's PATH. Ensure it's installed (e.g., `alsa-utils` for Linux).

---

## 🤝 Contributing

Suggestions and improvements are welcome! Feel free to open an issue to discuss a new feature or submit a pull request.

---

## A Note on the Learning Process

This project was created as a hands-on exercise to develop my programming skills. It started as a basic terminal script and evolved through various iterations, covering desktop notifications, sound integration, project organization, virtual environments, web interfaces with Flask, and cross-platform compatibility.

I want to be transparent about the process: I used an AI assistant as a tool to help write and, more importantly, *explain* the code. My goal was to learn how to code *with* AI, using it as a learning partner to grasp fundamentals step-by-step. This project is a result of that learning journey.