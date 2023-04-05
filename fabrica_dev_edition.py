# Exemplo inicial Franzininho WiFi com CircuitPython 
# Para mais detalhes sobre o CircuitPython, 
# acesse: https://circuitpython.org 
# Participe da comunidade Franzininho no Discord: https://discord.gg/sDZ9d98Kud
# Site do Projeto Franzinho: www.franzininho.com.br


import board
import neopixel_write
import digitalio
import time

pin = digitalio.DigitalInOut(board.NEOPIXEL)
pin.direction = digitalio.Direction.OUTPUT
pixel_off = bytearray([0, 0, 0])
pixel_green = bytearray([255, 0, 0])
pixel_red = bytearray([0, 255, 0])
pixel_blue = bytearray([0, 0, 255])


while True:
	neopixel_write.neopixel_write(pin, pixel_green)
	time.sleep(0.1)
	neopixel_write.neopixel_write(pin, pixel_off)
	time.sleep(1)
	neopixel_write.neopixel_write(pin, pixel_red)
	time.sleep(0.1)
	neopixel_write.neopixel_write(pin, pixel_off)
	time.sleep(1)
	neopixel_write.neopixel_write(pin, pixel_blue)
	time.sleep(0.1)
	neopixel_write.neopixel_write(pin, pixel_off)
	time.sleep(1)
	print("Voce acaba de receber uma placa Franzininho WiFi - Dev Edition")
	print("Aproveite a jornada!")
	print("Mais informações em: www.franzininho.com.br")
	print(" ")
