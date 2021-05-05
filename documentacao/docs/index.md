# Primeiros passos

Este documento tem como objetivo ajudá-lo a configurar o Franzininho WIFI para o uso no CircuitPython em seu computador.  Provavelmente ao inserir sua placa apareceu como uma unidade de disco. Confira a seguir mais instruções para o isso!

## Introdução

Antes de começar a diversão de programar a Franzininho WIFI e o CircuitPython, precisamos realizar alguns passos de configuração para determinado sistema. Veja abaixo o sistema e faça o passo a passo!

## Instalação

Nesta etapa vamos preparar o ambiente para você usar sua placa Franzininho WIFI, escolha seu sistema operacional e siga o passo a passo de como fazer esta configuração.

#### Windows

Para a instalação no windows você deve seguir o passo a passo deste tutorial.

1. Acesse o site, acesse este link: https://codewith.mu/ e clique em Download:

![imagem1](img/00/imagem1.png)   

2. Após isso clique na opção **Windows Installer**.

![imagem2](img/00/imagem2.png)

3. Salve em seu computador.

![imagem3](img/00/imagem3.png)

4. Aguarde até fazer o download e após isso clique em abrir o arquivo que você acabou de baixar.

![imagem4](img/00/imagem4.png)

5. Ao abrir o programa, irá aparecer uma tela onde você terá que aceitar os termos de uso do software, clique na caixa de seleção.

![imagem5](img/00/imagem5.png)

6. Então o botão de **install** será ativado, clique nele.

![imagem6](img/00/imagem6.png)

7. Aguarde a instalação.

![imagem7](img/00/imagem7.png)

8. Procure em seu computador **Mu Editor**

![imagem8](img/00/imagem8.png)

9. Então ao abrir uma janela, escolha **Circuit Python**, conforme a imagem abaixo:

![imagem9](img/00/imagem9.png)

![imagem10](img/00/imagem10.png)


10. Pronto, agora é só se divertir!


![imagem11](img/00/imagem11.png)


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
