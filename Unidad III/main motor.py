from machine import Pin
import time
import network
from umqtt.simple import MQTTClient

# Configuración WiFi
WIFI_SSID = "UTNG_GUEST"
WIFI_PASSWORD = "R3d1nv1t4d0s#UT"

# Configuración MQTT
MQTT_BROKER = "broker.emqx.io"
MQTT_TOPIC = "firealarm/emergencia"
CLIENT_ID = "esp32_relay"

# Configuración del Relay
relay = Pin(13, Pin.OUT)  # GPIO13 como salida
relay.value(1)  # Inicia con relé APAGADO (motor OFF)

# Función para conectar a WiFi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Conectando a WiFi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while not sta_if.isconnected():
            time.sleep(0.5)
    print("Conexión WiFi establecida:", sta_if.ifconfig())

# Callback para mensajes MQTT
def mqtt_callback(topic, msg):
    print("Mensaje recibido:", topic, msg)
    if msg == b'1':
        print("Encendiendo relay por 7 segundos")
        relay.value(0)  # Encender relay
        time.sleep(7)
        relay.value(1)  # Apagar después de 7 segundos
    elif msg == b'2':
        print("Encendiendo relay por 7 segundos")
        relay.value(0)  # Encender relay
        time.sleep(7)
        relay.value(1)  # Apagar después de 7 segundos
    else:
        print("Manteniendo estado actual del relay")

# Configurar y conectar MQTT
def setup_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(MQTT_TOPIC)
    print("Conectado al broker MQTT, suscrito a", MQTT_TOPIC)
    return client

# Programa principal
try:
    connect_wifi()
    mqtt_client = setup_mqtt()
    
    while True:
        print ("sin registros")
        mqtt_client.check_msg()  # Verificar mensajes entrantes
        time.sleep(1)  # Pequeña pausa para evitar sobrecarga

except Exception as e:
    print("Error:", e)
    relay.value(1)  # Asegurar que el relay se apague en caso de error