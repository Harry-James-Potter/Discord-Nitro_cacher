#  IMPORTING MODULES
import random, string, time, webbrowser, pyautogui
from pynput import keyboard
from playsound import playsound

keyboardd = keyboard.Controller()
no_of_links, i = 0, 0

#  FUNC WHICH GENERATES LINK
def NitroCode():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'

#  CLOSE TAB FUNC
def clik():
    keyboardd.press(keyboard.Key.ctrl)
    keyboardd.press("w")
    time.sleep((.1))
    keyboardd.release(keyboard.Key.ctrl)
    keyboardd.release("w")

webbrowser.open("https://www.google.com")
while not i == 1:
    no_of_links += 1
    Nitro = NitroCode()
    print(f"{no_of_links}) {Nitro}")
    webbrowser.open(Nitro)
    try:
        tim = time.time()
        time.sleep(1)
        while not pyautogui.pixel(678, 316) == (79, 84, 92):
            """
            This is the pixel value of point of poo, 
            x and y coordinates might be different on yours
            """
            if time.time() - tim >= 30:
                i = 1
                print(f"Nitro link is: {Nitro}")
                break
            continue
        clik()
    except WindowsError:
        continue

#  ALARM / ANY MUSIC AFTER THE RIGHT NITRO IS CREATED
playsound("")
