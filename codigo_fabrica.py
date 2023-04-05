# Exemplo inicial Franzininho WiFi com CircuitPython 
# Para mais detalhes sobre o CircuitPython, 
# acesse: https://circuitpython.org 
# Participe da comunidade Franzininho no Discord: https://discord.gg/sDZ9d98Kud
# Site do Projeto Franzinho: www.franzininho.com.br


import board
import time
from digitalio import DigitalInOut, Direction

# Configurando os pinos dos LEDs
led21 = DigitalInOut(board.IO21)
led21.direction = Direction.OUTPUT

led33 = DigitalInOut(board.IO33)
led33.direction = Direction.OUTPUT



while True:
	led21.value = True
	led33.value = False
    	time.sleep(0.5)
    	led21.value = False
    	led33.value = True
    	time.sleep(0.5)
	print("Voce acaba de receber uma placa Franzininho WiFi")
	print("Aproveite a jornada!")
	print("Mais informações em: www.franzininho.com.br")
	print(" ")
