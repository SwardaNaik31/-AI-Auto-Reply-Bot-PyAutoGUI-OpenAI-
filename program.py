import pyautogui
import time
import pyperclip
from openai import OpenAI
import os

pyautogui.FAILSAFE = True   # enable safety
pyautogui.PAUSE = 0.5      # avoid freezing

print("You have 5 seconds. Switch to Chrome and SELECT TEXT.")
time.sleep(5)


# Copy selected text
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

text = pyperclip.paste().strip()
print("Copied text:\n", text)

if not text:
    print("❌ No text copied. Select text first.")
    exit()

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Reply briefly and clearly."},
        {"role": "user", "content": text}
    ]
)

reply = response.choices[0].message.content
print("AI Reply:\n", reply)

# Paste reply
pyperclip.copy(reply)
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
