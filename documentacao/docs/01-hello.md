# Hello World(Pisca LED)

![imagem_hello_world.png](img/01/imagem_hello_world.png)

## Proposta da atividade

 O primeiro contato com a Franzininho WIFI será para você fazer um blink (que faz com que o LED pisque em intervalos de tempo). Assim, você irá fazer seu primeiro **Hello, World**! em um hardware.

## Materiais

-   1 Placa Franzininho WIFI;
-   1 Protoboard;
-   1 LED 3mm;
-   1 Resistor 330 Ohm;
-   Jumpers

![circuito](img/01/circuito.png)

## Código


```python
"""Lição 1: Lição 1 - Hello World(Pisca LED)"""  
import board  
import time from digitalio import DigitalInOut, Direction  

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

Confira um breve vídeo aplicando o pisca LED em miniatura com relação ao nosso cotidiano.

<iframe width="560" height="315" src="https://www.youtube.com/embed/tgY2_n1aOC4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


## Desafio

Agora que você aprendeu a fazer o **Hello, World** com a Franzininho WIFI, desafiamos você a piscar outro LED simultaneamente.


!!! note " Dica "
    Utilize a ```#franzininho```  para que nós possamos publicar em nossas redes sociais o seu desafio
