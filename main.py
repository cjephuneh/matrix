import pyautogui
import time

# Ensuring the failsafe is on, so you can stop the script by moving the mouse to the upper left corner.
pyautogui.FAILSAFE = True

while True:
    # Move the mouse cursor in a small pattern
    pyautogui.move(100, 0, duration=1)  # Right
    pyautogui.move(0, 100, duration=1)  # Down
    pyautogui.move(-100, 0, duration=1)  # Left
    pyautogui.move(0, -100, duration=1)  # Up

    # Press the 'shift' key after moving the mouse
    pyautogui.press('shift')

    # Wait for 5 seconds before moving the mouse again
    time.sleep(5)
