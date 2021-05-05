# Primeiros passos

Este documento tem como objetivo ajudá-lo a configurar o Franzininho WIFI para o uso no CircuitPython em seu computador.  Provavelmente ao inserir sua placa apareceu como uma unidade de disco. Confira a seguir mais instruções para o isso!

## Introdução

Para iniciar o CircuitPython é importante você entender como interagir com REPL, antes de usar um editor. O primeiro passo é utilizar via terminal serial e depois a como utiliza-lo no editor MU. No próximo tópico vamos aprender a como usar o REPL através do terminal serial.

## Terminal

O primeiro passo é conectar a placa Franzininho Wifi em seu computador e logo irá aparecer algo parecido com um dispositivo de pen drive, conforme a imagem abaixo:


![alt_text](img/00/primeiros_passos_1.png "image_tooltip")


Antes de sair abrindo os arquivos, faça o seguinte passo:


1 - Conecte a Franzininho

2 - Abra o terminal

3 - Instale um terminal, por exemplo, para instalar o picocom, digite os comandos abaixo:


```
sudo apt-get update
sudo apt-get install picocom
```

4 - Para acessar o terminal serial, digite o seguinte comando: picomcom /dev/ttyACM0 de enter.


![alt_text](img/00/primeiros_passos_2.png "image_tooltip")

5 - Agora aperte  o Ctrl C do teclado e então aparecerá >>>

![alt_text](img/00/primeiros_passos_3.png "image_tooltip")


6 -  No terminal digite: print(“Hello World”) e aperte o enter (você pode escrever qualquer coisa dentro das aspas, então aparecerá o que você escreveu.

![alt_text](img/00/primeiros_passos_4.png "image_tooltip")

7 - Agora vamos fazer uma operação matemática, digite um valor | escolha uma operação matemática e digite outro valor, aperte o enter e veja o resultado, conforme a imagem:


![alt_text](img/00/primeiros_passos_5.png "image_tooltip")


8 - Agora digite o seguinte código no terminal:

```python
import board
dir(board)
```

Então aparecerá o conjunto de pinos disponíveis na Franzininho Wifi.


![alt_text](img/00/primeiros_passos_6.png "image_tooltip")


Agora que você já sabe quais são os nomes dos pinos da placa e também interagir com REPL. Podemos fechar o terminal e dar início abrindo o arquivo **code.py** que está na pasta.


![alt_text](img/00/primeiros_passos_7.png "image_tooltip")
