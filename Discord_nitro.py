# CURRENTLY WORKING
import random, string, time, webbrowser, pyautogui
from pynput import keyboard
keyboardd = keyboard.Controller()
no_of_links = 0
while True:
    def NitroCode():
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
        return f'https://discord.gift/{code}'
    no_of_links += 1
    print(f"{no_of_links}) {NitroCode()}")
    webbrowser.open(NitroCode())
    try:
        while not pyautogui.pixel(678, 316) == (79, 84, 92):
            """
            This is the pixel value of point of poo, 
            x and y coordinates might be different on yours
            """
            continue
    except WindowsError:
        continue
    keyboardd.press(keyboard.Key.ctrl)
    keyboardd.press("w")
    time.sleep(0.25)
    keyboardd.release(keyboard.Key.ctrl)
    keyboardd.release("w")
