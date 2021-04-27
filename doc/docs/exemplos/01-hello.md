# Hello World(Pisca LED)

## Proposta da atividade

 O primeiro contato com a Franzininho WIFI será você fazer o blink (que faz com que o LED pisque em intervalos de tempo). Assim teremos o primeiro contato em fazer seu primeiro **Hello, World**! em um Hardware.

## Materiais

-   1 Placa Franzininho WIFI;
-   1 Protoboard;
-   1 LED 3mm;
-   1 Resistor 330 Ohm;
-   Jumpers

![circuito](/doc/docs/images/01/01-circuito.png)

## Código


```python
"""Lição 1: Lição 1 - Hello World(Pisca LED)"""  
import board  
import time  
from digitalio import DigitalInOut, Direction  

# Configurando o pino do LED

# o led que configurei foi o pino 4 = IO4  
led = DigitalInOut(board.IO4)  
led.direction = Direction.OUTPUT  

#loop infinito - executando sempre  
while  True:  
  led.value = True  
  time.sleep(0.5)  
  led.value = False  
  time.sleep(0.5)
```

## Video

## Desafio

Agora que você aprendeu a fazer o **Hello, World** com a Franzininho WIFI, desafiamos você a piscar outro LED simultaneamente.


Utilize a `#franzininhowifi`  para que nós possamos publicar em nossas redes sociais o seu desafio.
