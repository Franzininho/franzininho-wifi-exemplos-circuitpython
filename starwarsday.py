import time
import board
import pwmio
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import neopixel

pixel_pin = board.IO7
num_pixels = 13
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False)

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

c = 261
d = 294
e = 329
f = 349
g = 391
gS = 415
a = 440
aS = 455
b = 466
cH = 523
cSH = 554
dH = 587
dSH = 622
eH = 659
fH = 698
fSH = 740
gH = 784
gSH = 830
aH = 880


# For the M0 boards:
piezo = pwmio.PWMOut(board.IO6, duty_cycle=0, frequency=440, variable_frequency=True)

def beep(nota,tempo):
    piezo.frequency = nota
    piezo.duty_cycle = 65535 // 2  # On 50%
    time.sleep(tempo)  # On for 1/4 second
    piezo.duty_cycle = 0  # Off
    time.sleep(0.05)  # Pause between notes



def firstSection():
    beep(a, 0.500);
    beep(a, 0.500);
    beep(a, 0.500);
    beep(f, 0.350);
    beep(cH, 0.150);
    beep(a, 0.500);
    beep(f, 0.350);
    beep(cH, 0.150);
    beep(a, 0.650);

    time.sleep(0.5)  # Pause between notes

    beep(eH, 0.500);
    beep(eH, 0.500);
    beep(eH, 0.500);
    beep(fH, 0.350);
    beep(cH, 0.150);
    beep(gS, 0.500);
    beep(f, 0.350);
    beep(cH, 0.150);
    beep(a, 0.650);

    time.sleep(0.5)  # Pause between notes

def secondSection():
    beep(aH, 0.500);
    beep(a,  0.300);
    beep(a,  0.150);
    beep(aH,  0.500);
    beep(gSH,  0.325);
    beep(gH,  0.175);
    beep(fSH,  0.125);
    beep(fH,  0.125);
    beep(fSH,  0.250);

    time.sleep(0.325)  # Pause between notes

    beep(aS,  0.250);
    beep(dSH,  0.500);
    beep(dH,  0.325);
    beep(cSH,  0.175);
    beep(cH,  0.125);
    beep(b,  0.125);
    beep(cH,  0.250);

    time.sleep(0.35)  # Pause between notes

def thirdSection():
    beep(f, 0.250);
    beep(gS, 0.500);
    beep(f, 0.350);
    beep(a, 0.125);
    beep(cH, 0.500);
    beep(a, 0.375);
    beep(cH, 0.125);
    beep(eH, 0.650);

    time.sleep(0.5)  # Pause between notes

def fourthSection():
    beep(f, 0.250);
    beep(gS, 0.500);
    beep(f, 0.375);
    beep(cH, 0.125);
    beep(a, 0.500);
    beep(f, 0.375);
    beep(cH, 0.125);
    beep(a, 0.650);

    time.sleep(0.65)  # Pause between notes



while True:
    pixels.fill(GREEN)
    pixels.show()
    firstSection()
    pixels.fill(CYAN)
    pixels.show()
    secondSection()
    pixels.fill(PURPLE)
    pixels.show()
    thirdSection()
    pixels.fill(RED)
    pixels.show()
    secondSection()
    pixels.fill(YELLOW)
    pixels.show()
    fourthSection()

    time.sleep(2)

