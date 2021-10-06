# Exemplo para publicação de valores do DHT11 para o Adafruit IO
# Autor: Fábio Souza
#data: 05/10/21

import board
import time

#DHT
import adafruit_dht
dht = adafruit_dht.DHT11(board.IO2)

#WiFi
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT
from adafruit_io.adafruit_io import IO_MQTT

# Adicione um arquivo secrets.py ao seu sistema de arquivos que tenha um dicionário chamado secrets com "ssid" e
#"password" com suas credenciais WiFi.  NÃO compartilhe esse arquivo ou envie-o para Git ou outro
# fonte de controle.
try:
    from secrets import secrets
except ImportError:
    print("As credenciais do WiFi são mantidos em secrets.py, adicione-os lá!")
    raise

# Defina seu nome de usuário e chave Adafruit IO em secrets.py
# (visite io.adafruit.com se precisar criar uma conta,
# ou se você precisar de sua chave Adafruit IO.)
aio_username = secrets["aio_username"]
aio_key = secrets["aio_key"]

print("Conectando à %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Conectado a %s!" % secrets["ssid"])

# Defina funções de callback que serão chamadas quando certos eventos acontecerem.
def connected(client):
    print("Conectado ao Adafruit IO!")
    # Inscreva-se para receber alterações nos feeds
    client.subscribe("sensorTemperatura")
    client.subscribe("sensorUmidade")


def subscribe(client, userdata, topic, granted_qos):
    # Este método é chamado quando o cliente assina um novo feed.
    print("Inscrito em {0} com QOS level {1}".format(topic, granted_qos))


def unsubscribe(client, userdata, topic, pid):
    # Este método é chamado quando o cliente cancela a assinatura de um feed.
    print("Cancelamento de inscrição em {0} com PID {1}".format(topic, pid))


def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print("Desconectado da Adafruit IO!")


def message(client, feed_id, payload):
    # A função de mensagem será chamada quando um feed inscrito tiver um novo valor.
     # O parâmetro feed_id identifica o feed, e o parâmetro de payload tem
     # o novo valor.
    print("Feed {0} received new value: {1}".format(feed_id, payload))


# Cria uma socketpool
pool = socketpool.SocketPool(wifi.radio)

# Inicializar um novo objeto MQTT Client
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    username=secrets["aio_username"],
    password=secrets["aio_key"],
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Inicializa um cliente MQTT no Adafruit IO 
io = IO_MQTT(mqtt_client)

# Conecte os métodos de retorno de chamada definidos acima para Adafruit IO
io.on_connect = connected
io.on_disconnect = disconnected
io.on_subscribe = subscribe
io.on_unsubscribe = unsubscribe
io.on_message = message

# Conecta ao Adafruit IO
print("Conectando-se ao Adafruit IO ...")
io.connect()

# Abaixo está um exemplo de publicação dos valores de temperatura e umidade para Adafruit IO.
last = 0
print("Publicando uma nova mensagem a cada 30 segundos ...")
while True:
    # função de atualização do Adafruit IO
    io.loop()
    # Envia uma mensagem a cada 30 segundos
    if (time.monotonic() - last) >= 30:
        try:
            temperature = dht.temperature
            humidity = dht.humidity
            # Imprima valores no REPL
            print("Publicando {0} em sensorTemperatura.".format(temperature))
            print("Publicando {0} em sensorUmidade.".format(humidity))
            # Publica valores no adafruit IO
            io.publish("sensorTemperatura", temperature)
            io.publish("sensorUmidade", humidity)
        except RuntimeError as e:
            # Se leitura falhar, Basta imprimir o erro e tentaremos novamente
            print("Falha na Leitura do DHT: ", e.args)
        
        last = time.monotonic()