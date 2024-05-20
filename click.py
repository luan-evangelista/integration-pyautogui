import pyautogui

# Custom click
pyautogui.click(x=1600,y=126,clicks=2,interval=1, button='right',duration=2)

# Click on the current position (with left button)
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')

# Click X times
pyautogui.click(clicks=10)

# Functions ready for clicks
pyautogui.doubleClick()
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.tripleClick()