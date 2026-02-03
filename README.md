🤖 AI Auto Reply Bot (Python + PyAutoGUI + OpenAI)

    An AI-powered desktop automation tool that copies selected on-screen text, generates an intelligent reply using OpenAI, and automatically pastes and sends the response.
    This project also includes a mouse position helper to make PyAutoGUI automation easier and more accurate.

✨ Features:

    📋 Copy selected text from any application
    🧠 Generate AI-based replies using OpenAI
    ⌨️ Automatically paste and send replies
    🛡️ PyAutoGUI fail-safe enabled
    📍 Mouse position tracking utility
    🔐 Secure API key handling (environment variables)

🛠️ Tech Stack:

    Python 3.10+
    PyAutoGUI
    Pyperclip
    OpenAI Python SDK

Install required libraries:

 pip install pyautogui pyperclip openai

🔑 OpenAI API Key Setup (Required)
⚠️ Never hard-code your API key:

    Windows (PowerShell)
    setx OPENAI_API_KEY "sk-your-api-key-here"

▶️ How to Run the Auto-Reply Bot:

     Open Chrome (or any app)
    Select the text you want the AI to reply to
Run:

python program.py
You have 5 seconds to switch back and ensure text is selected
The bot will automatically:
Copy the text
Generate an AI reply
Paste and send it

main.py file is used to find coordinates of the screen using mouse movement
program.py is the main file which contains autoreply code

