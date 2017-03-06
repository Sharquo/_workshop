__author__ = 'alex.taxter'

import pyautogui, subprocess, time

subprocess.Popen('C:\\Program Files\\IntPetro44\\IntPetro.exe')

# Setup failsafe - move mouse to upper left to abort program
pyautogui.FAILSAFE = True

time.sleep(34.5)
# IP takes way too long to load up :-/

pyautogui.press(['alt', 'space', 'x'])

# Launch clay volume
pyautogui.press(['alt', 'i', 'c'])

# Set up values and run
pyautogui.press(['enter', 'enter'])

# Maximise the resulting log plot
pyautogui.click(x=775, y=135, clicks=1, button='left')