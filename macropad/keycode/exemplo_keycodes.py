#exemplo1

import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kbd = Keyboard(usb_hid.devices)

key1 = digitalio.DigitalInOut(board.IO7)
key1.direction = digitalio.Direction.INPUT
key1.pull = digitalio.Pull.UP

key2 = digitalio.DigitalInOut(board.IO6)
key2.direction = digitalio.Direction.INPUT
key2.pull = digitalio.Pull.UP

key3 = digitalio.DigitalInOut(board.IO5)
key3.direction = digitalio.Direction.INPUT
key3.pull = digitalio.Pull.UP

key4 = digitalio.DigitalInOut(board.IO4)
key4.direction = digitalio.Direction.INPUT
key4.pull = digitalio.Pull.UP

key5 = digitalio.DigitalInOut(board.IO3)
key5.direction = digitalio.Direction.INPUT
key5.pull = digitalio.Pull.UP

key6 = digitalio.DigitalInOut(board.IO2)
key6.direction = digitalio.Direction.INPUT
key6.pull = digitalio.Pull.UP

while True:
    if key1.value == False:
        kbd.send(Keycode.WINDOWS, Keycode.TAB)

    if key2.value == False:
        kbd.send(Keycode.CONTROL, Keycode.C)

    if key3.value == False:
        kbd.send(Keycode.CONTROL, Keycode.V)
          
    if key4.value == False:
        kbd.send(Keycode.RIGHT_ARROW)
        
    if key5.value == False:
        kbd.send(Keycode.SPACEBAR)
        
    if key6.value == False:
        kbd.press(Keycode.DOWN_ARROW)
    else:
        kbd.release(Keycode.DOWN_ARROW)

    time.sleep(0.1)
