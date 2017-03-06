__author__ = 'alex.taxter'

import pyautogui, subprocess, time

subprocess.Popen('C:\\Program Files\\IntPetro43\\IntPetro.exe')

# Setup failsafe - move mouse to upper left to abort program
pyautogui.FAILSAFE = True

time.sleep(34.5)
# IP takes way too long to load up :-/

pyautogui.press(['alt', 'space', 'x'])

# Launch MW notes
pyautogui.press(['alt', 'u', 'v'])

# Select all available wells.  Hotkeys are kinda awful here.
pyautogui.press(['tab', 'tab', 'tab'])


pyautogui.press(['down', 'up'])

pyautogui.keyDown('shift')
pyautogui.press(['down', 'down'])
pyautogui.keyUp('shift')

pyautogui.click(990, 440, clicks=1, button='left')

pyautogui.press('enter')
