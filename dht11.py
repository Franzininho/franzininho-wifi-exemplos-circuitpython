""" Leitura de temperatura e umidade com DHT11 """

import board
import time
import adafruit_dht

dht = adafruit_dht.DHT11(board.IO2)

while True:
    try:
        temperatura = dht.temperature
        umidade = dht.humidity
        # Imprime valores lidos na serial
        print("Temperatura: {:.1f} °C \t Umidade: {}%".format(temperatura, umidade))
    except RuntimeError as e:
        # A leitura do DHT11 pode falhar
        print("Falha na leitura do DHT11: ", e.args)

    time.sleep(1)

