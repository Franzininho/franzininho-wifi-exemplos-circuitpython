import time
import board
import touchio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode

touch_pad = board.IO14
touch = touchio.TouchIn(touch_pad)
touch.threshold = 50535

touch_pad = board.IO1
touch2 = touchio.TouchIn(touch_pad)
touch2.threshold = 50535


# The keyboard object!
time.sleep(2)  # Sleep for a bit to avoid a race condition on some systems
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)  # We're in the US :)

print("Waiting for key pin...")

while True:
    if touch.value:
        keyboard.press(Keycode.SPACEBAR)  # "Press"...
        keyboard.release_all()  # ..."Release"!

    if touch2.value:
        keyboard.press(Keycode.DOWN_ARROW)  # "Press"...
        #keyboard.release_all()  # ..."Release"!

    time.sleep(0.05)