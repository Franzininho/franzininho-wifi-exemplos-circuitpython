import time

import adafruit_dht
import board

dht = adafruit_dht.DHT11(board.IO2)

while True:
    try:
        temperature = dht.temperature
        humidity = dht.humidity
        # Print what we got to the REPL
        print(temperature)
        print(humidity)
    except RuntimeError as e:
        # Reading doesn't always work! Just print error and we'll try again
        print("Reading from DHT failure: ", e.args)

    time.sleep(1)

