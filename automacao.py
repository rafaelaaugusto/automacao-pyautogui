
import webbrowser
import pyautogui
import time

time.sleep(3)

# Email
webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
time.sleep(3)
# Abre plataforma da Digital Innovation One
webbrowser.open("https://web.digitalinnovation.one/home")
time.sleep(5)

# Abre a plataforma da mesttra
webbrowser.open("https://app.mesttra.com/dashboard")
time.sleep(4)

# Abrir VS Code
pyautogui.hotkey("winleft")
pyautogui.write("Visual")
time.sleep(1)
pyautogui.press("enter")

