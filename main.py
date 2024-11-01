import pyautogui
import time

time.sleep(5)

pyautogui.hotkey('win', 'd')
time.sleep(1)
pyautogui.hotkey('win', 'r')
time.sleep(1)
pyautogui.write('taskkill /f /im explorer.exe')
time.sleep(1)
pyautogui.press('enter')
