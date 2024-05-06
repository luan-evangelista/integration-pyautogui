import pyautogui
from time import sleep

pyautogui.moveTo(388,531,duration=2)
# pyautogui.move(45,0,duration=1)
for i in range(100):
    sleep(0.1)
    pyautogui.click()
