
import webbrowser
import pyautogui
#import pyperclip
import time

time.sleep(3)

# Email
webbrowser.open("https://mail.google.com/mail/u/1/#inbox")
time.sleep(3)
# Abrir Digital Innovation
webbrowser.open("https://web.digitalinnovation.one/home")
time.sleep(5)

# Abre a mesttra
webbrowser.open("https://app.mesttra.com/dashboard")
time.sleep(4)

# Abrir VS code
pyautogui.hotkey("winleft")
pyautogui.write("Visual")
time.sleep(1)
pyautogui.press("enter")

