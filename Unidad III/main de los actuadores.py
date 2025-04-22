from machine import Pin, PWM
import neopixel
import time
import ujson
from umqtt.simple import MQTTClient
import network

# Configuración de hardware
NUM_LEDS = 15
np = neopixel.NeoPixel(Pin(5), NUM_LEDS)  # Asume que la tira LED está en el pin 13
led_rojo = Pin(13, Pin.OUT)               # LED rojo en pin 12
led_verde = Pin(12, Pin.OUT)              # LED verde en pin 14
buzzer_circuito = PWM(Pin(14))            # Buzzer en circuito en pin 25
buzzer_control = PWM(Pin(15))             # Buzzer en control en pin 26
boton = Pin(4, Pin.IN, Pin.PULL_UP)     # Botón en pin 27

# Configuración MQTT
MQTT_BROKER = "broker.emqx.io"     # Cambiar por la dirección de tu broker
CLIENT_ID = "esp32_firealarm"
TOPIC = "firealarm/emergencia"

# Estados
ESTADO_NORMAL = 0
ESTADO_MANUAL = 1
ESTADO_EMERGENCIA = 2

estado_actual = ESTADO_NORMAL
ultimo_cambio_estado = 0

# Colores (R, G, B)
COLOR_VERDE_LIMA = (50, 255, 0)
COLOR_NARANJA = (255, 50, 0)
COLOR_ROJO = (255, 0, 0)

def conectar_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Conectando a WiFi...')
        sta_if.active(True)
        sta_if.connect('UTNG_GUEST', 'R3d1nv1t4d0s#UT')  # Cambia por tus credenciales
        while not sta_if.isconnected():
            time.sleep(0.5)
            print('.', end='')
    print('\nConfiguración de red:', sta_if.ifconfig())

# Configuración MQTT
def conectar_mqtt():
    client = MQTTClient(CLIENT_ID, MQTT_BROKER)
    client.set_callback(mqtt_callback)
    client.connect()
    client.subscribe(TOPIC)
    print("Conectado a MQTT Broker")
    return client

def mqtt_callback(topic, msg):
    global estado_actual, ultimo_cambio_estado
    mensaje = msg.decode()
    print(f"Mensaje recibido en {topic}: {mensaje}")
    
    if topic.decode() == TOPIC:
        if mensaje == "1" and estado_actual != ESTADO_EMERGENCIA:
            cambiar_estado(ESTADO_MANUAL)
        elif mensaje == "2":
            cambiar_estado(ESTADO_EMERGENCIA)

def cambiar_estado(nuevo_estado):
    global estado_actual, ultimo_cambio_estado
    estado_actual = nuevo_estado
    ultimo_cambio_estado = time.time()
    print(f"Cambiando a estado {estado_actual}")

def publicar_mensaje(client, mensaje):
    try:
        client.publish(TOPIC, mensaje)
        print(f"Mensaje publicado: {mensaje}")
    except Exception as e:
        print(f"Error al publicar: {e}")

# Funciones de control de hardware
def set_led_strip(color):
    for i in range(NUM_LEDS):
        np[i] = color
    np.write()

def beep(buzzer, frecuencia, duracion=0.1):
    buzzer.freq(frecuencia)
    buzzer.duty(512)
    time.sleep(duracion)
    buzzer.duty(0)

def parar_buzzer():
    buzzer_circuito.duty(0)
    buzzer_control.duty(0)

def estado_normal():
    set_led_strip(COLOR_VERDE_LIMA)
    led_verde.on()
    led_rojo.off()
    parar_buzzer()

def estado_manual():
    set_led_strip(COLOR_NARANJA)
    led_verde.off()
    led_rojo.on()
    # Buzzer intermitente (solo el del circuito)
    beep(buzzer_circuito, 800, 0.2)
    time.sleep(0.3)

def estado_emergencia():
    set_led_strip(COLOR_ROJO)
    led_verde.off()
    led_rojo.on()
    # Ambos buzzers intermitentes
    beep(buzzer_circuito, 1000, 0.2)
    beep(buzzer_control, 1200, 0.2)
    time.sleep(0.3)

# Manejo del botón
def leer_boton():
    global estado_actual
    tiempo_presionado = 0
    inicio_presion = 0
    
    if boton.value() == 0:  # Botón presionado (asumiendo pull-up)
        inicio_presion = time.time()
        while boton.value() == 0:
            time.sleep(0.1)
            tiempo_presionado = time.time() - inicio_presion
            if tiempo_presionado >= 3:
                # Botón presionado por más de 3 segundos
                if estado_actual == ESTADO_NORMAL:
                    print("Activación manual detectada")
                    publicar_mensaje(client, "1")
                    cambiar_estado(ESTADO_MANUAL)
                break

# Inicialización
def inicializar():
    global client
    estado_normal()
    conectar_wifi()
    client = conectar_mqtt()
    print("Sistema inicializado")

# Bucle principal
def main():
    inicializar()
    try:
        while True:
            client.check_msg()  # Verificar mensajes MQTT
            leer_boton()        # Verificar estado del botón
            
            # Manejo de estados
            if estado_actual == ESTADO_NORMAL:
                estado_normal()
            elif estado_actual == ESTADO_MANUAL:
                estado_manual()
                if time.time() - ultimo_cambio_estado >= 10:
                    cambiar_estado(ESTADO_NORMAL)
            elif estado_actual == ESTADO_EMERGENCIA:
                estado_emergencia()
                if time.time() - ultimo_cambio_estado >= 10:
                    cambiar_estado(ESTADO_NORMAL)
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("Apagando sistema...")
        estado_normal()
        client.disconnect()

if __name__ == "__main__":
    main()