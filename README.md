# Simple Desktop Reminder App ⏰

A minimalist, cross-platform desktop application that sends persistent system notifications with an audible alert. Set and manage your reminders from a simple graphical user interface.

## ✨ Features

- **Simple GUI:** Easy-to-use window with input fields and buttons, built with Python's native Tkinter library.
- **Cross-Platform:** Designed to run seamlessly on Linux, Windows, and macOS.
- **Customizable Reminders:** Set any task and a custom interval (in seconds).
- **Desktop Notifications:** Uses your operating system's native notification system for visual alerts.
- **System Default Sound:** Plays your OS's default alert sound with each notification. No audio files needed!
- **Self-Contained:** The application requires no external files (like `.wav` files) to function.
- **Executable Packaging:** Can be bundled into a single executable file for easy distribution to users.

---

## 🛠️ How It Works (Tech Stack)

This project is built with fundamental Python libraries to provide a straightforward desktop experience.

- **Python 3:** The core programming language.
- **Tkinter:** Python's standard library for building the graphical user interface and playing the system's default alert sound (`app.bell()`).
- **`plyer`:** A cross-platform library for sending desktop notifications.
- **`threading`:** Python's standard library for running the reminder in the background so the app doesn't freeze.

---

## 🚀 Getting Started (Setup & Usage)

To run this project on your machine, follow these steps.

### 1. System Prerequisites

- **Linux (e.g., Arch):**
  - Ensure you have `python`, `python-pip`, and the `tk` package for the GUI installed.
    ```bash
    sudo pacman -S python python-pip tk
    ```
  - (Optional) For better `plyer` integration and to remove a common warning, install `python-dbus`: `sudo pacman -S python-dbus`.
- **Windows:**
  - Install Python 3 from [python.org](https://www.python.org/downloads/windows/), ensuring you check "Add Python to PATH" and that the "tcl/tk and IDLE" option is selected during installation.
- **macOS:**
  - Install Python 3 using Homebrew (`brew install python`) to ensure a modern version of Tcl/Tk is included for the GUI.

### 2. Project Setup

1.  **Clone this repository (or use your existing project folder):**
    ```bash
    git clone https://github.com/your_username/simple-reminder-app.git # Replace with your GitHub username
    cd simple-reminder-app
    ```

2.  **Create and Activate a Virtual Environment:**
    This isolates the project's Python packages.
    ```bash
    python -m venv venv
    # On Linux/macOS:
    source venv/bin/activate
    # On Windows (CMD):
    # venv\Scripts\activate.bat
    ```
    Your terminal prompt should change to show `(venv)`.

3.  **Install Python Dependencies:**
    This installs `plyer`, the only external Python library needed.
    ```bash
    pip install -r requirements.txt
    ```

### 3. Running the App from Source

With your virtual environment active, run the application:
```bash
python reminder_app.py
A desktop window will appear. Use the interface to start and stop your reminders. To close the application completely, just close its window.
```

---

## 📦 Packaging for End-Users (Making it a ".exe" or ".app")

You can use **PyInstaller** to bundle your app into a single executable file, so users don't need to install Python or any dependencies.

1.  **Install PyInstaller** in your active virtual environment:
    ```bash
    pip install pyinstaller
    ```

2.  **Run the PyInstaller command:**
    ```bash
    pyinstaller --onefile --windowed reminder_app.py
    ```
    - `--onefile`: Bundles everything into a single executable.
    - `--windowed` (or `--noconsole` on Windows): Prevents a black console window from appearing behind your app.
    - **Note:** We no longer need `--add-data` because the app uses the system's built-in sound and requires no external files!

3.  **Find your app** in the `dist/` folder that PyInstaller creates. This is the file you can share with others!
    - **Linux:** `dist/reminder_app`
    - **Windows:** `dist/reminder_app.exe`
    - **macOS:** `dist/reminder_app.app` (an application bundle)

---

## ⚙️ Customization

Edit the reminder_app.py file to change the app's behavior:
   - Default Text: Change the text in task_entry.insert() and interval_entry.insert() to modify the default values in the input fields.
   - Window Size: Change the values in app.geometry("400x200").
   - Layout: Modify the .grid() calls for each widget to change its position.

---

## ⚠️ Troubleshooting

- **Window doesn't appear / Tkinter error:**
  - Ensure the `tk` package (or its equivalent for your OS/distro) is installed system-wide.

- **"ModuleNotFoundError: No module named 'plyer'":**
  - Make sure your virtual environment is active (`(venv)` in your terminal prompt).
  - Run `pip install -r requirements.txt` again.

- **No desktop notifications:**
  - Check your OS's notification settings (e.g., "Focus Assist" on Windows, "Do Not Disturb" modes on any OS).
  - On macOS, you might need to grant notification permissions for the application.
  - On Linux, consider installing `python-dbus` to improve `plyer` integration.

- **No sound:**
  - Check your system's master volume and audio output device. The sound played is your OS's default "alert" or "bell" sound.

- **Executable not working after PyInstaller:**
  - Try running the executable from the terminal (`./dist/reminder_app`) to see any error messages.
  - Building for one OS produces an executable for that OS only. You must build on Windows to get a `.exe`, on macOS for a `.app`, etc.

---

## A Note on the Learning Process

This project was created as a hands-on exercise to develop a cross-platform desktop application from scratch. It demonstrates core concepts like GUI development (Tkinter), background tasks (threading), and system interaction (notifications and sound). The goal was to create a simple, understandable, yet fully functional program. I used an AI assistant as a tool to help write and, more importantly, explain the code, using it as a learning partner to grasp fundamentals step-by-step.

---