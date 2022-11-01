import time
import board
import digitalio
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode


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


cc = ConsumerControl(usb_hid.devices)

while True:
    if key1.value == False:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        time.sleep(0.1)

    if key2.value == False:
        cc.send(ConsumerControlCode.BRIGHTNESS_DECREMENT)
        time.sleep(0.1)

    if key3.value == False:
        cc.send(ConsumerControlCode.BRIGHTNESS_INCREMENT)
        time.sleep(0.1)
          
    if key4.value == False:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT )
        time.sleep(0.1)
        
    if key5.value == False:
        cc.send(ConsumerControlCode.MUTE)
        time.sleep(0.1)
        
    if key6.value == False:
        cc.send(ConsumerControlCode.PLAY_PAUSE)
        time.sleep(0.1)

    time.sleep(0.1)


