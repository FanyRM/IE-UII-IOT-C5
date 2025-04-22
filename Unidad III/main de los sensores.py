from machine import Pin, SoftI2C, ADC
from mlx90614 import MLX90614
import time
import network
from umqtt.simple import MQTTClient
import ujson

# Configuración de sensores
# Sensor PIR
pir = Pin(34, Pin.IN)
ultimo_estado_pir = None

# Sensor MLX90614 (Termómetro Infrarrojo)
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
sensor_temp = MLX90614(i2c)

# Sensor MQ-2 (Densidad del aire)
mq2 = ADC(Pin(35))
mq2.atten(ADC.ATTN_11DB)  # Rango completo 0-3.3v
ultimo_estado_mq2 = None

# Umbrales para MQ-2
MQ2_NORMAL = 1500  # Valores por debajo son normales
MQ2_ALERTA = 2000  # Valores entre 1500-2000 son poco adecuados
                  # Valores por encima de 2000 son emergencia

# Umbrales para temperatura
TEMP_ALERTA = 50.0  # Grados Celsius para considerar emergencia

# Configuración WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('celeste', '12345678')
while not wifi.isconnected():
    time.sleep(0.5)

# Configuración MQTT
broker = "192.168.1.38"
client = MQTTClient("esp32_sensores", broker)

# Tópicos
TOPIC_ACTIVIDAD = b"firealarm/sensor/actividad"
TOPIC_TEMPERATURA = b"firealarm/sensor/temperaturas"
TOPIC_DENSIDAD = b"firealarm/sensor/densidad"
TOPIC_EMERGENCIA = b"firealarm/emergencia"

def conectar_mqtt():
    try:
        client.connect()
    except:
        print("Error al conectar MQTT, reintentando...")
        time.sleep(5)
        conectar_mqtt()

def leer_mq2():
    valor = mq2.read()
    
    if valor < MQ2_NORMAL:
        estado = "normal"
    elif valor < MQ2_ALERTA:
        estado = "poco_adecuada"
    else:
        estado = "emergencia"
    
    return valor, estado

def enviar_emergencia():
    try:
        client.publish(TOPIC_EMERGENCIA, b"2")
        print("¡Alerta de emergencia enviada!")
    except:
        print("Error al enviar emergencia")
        conectar_mqtt()

def enviar_datos_periodicos():
    global ultimo_estado_pir, ultimo_estado_mq2
    
    # Leer sensor PIR
    movimiento = pir.value()
    if movimiento or (ultimo_estado_pir is not None and ultimo_estado_pir != movimiento):
        mensaje = "movimiento_detectado" if movimiento else "sin_movimiento"
        try:
            client.publish(TOPIC_ACTIVIDAD, mensaje)
            print(f"Actividad PIR: {mensaje}")
        except:
            conectar_mqtt()
    ultimo_estado_pir = movimiento
    
    # Leer sensor de temperatura
    temp_obj = round(sensor_temp.read_object_temp(), 2)
    temp_amb = round(sensor_temp.read_ambient_temp(), 2)
    
    data_temp = {
        "temp_obj": temp_obj,
        "temp_amb": temp_amb
    }
    
    try:
        client.publish(TOPIC_TEMPERATURA, ujson.dumps(data_temp))
        print(f"Temperaturas: Obj={temp_obj}°C, Amb={temp_amb}°C")
    except:
        conectar_mqtt()
    
    # Leer sensor MQ-2
    valor_mq2, estado_mq2 = leer_mq2()
    data_mq2 = {
        "valor": valor_mq2,
        "estado": estado_mq2
    }
    try:
        client.publish(TOPIC_DENSIDAD, ujson.dumps(data_mq2))
        print(f"Densidad aire: {valor_mq2} ({estado_mq2})")
    except:
        conectar_mqtt()
    
    # Verificar condiciones de emergencia
    if estado_mq2 == "emergencia" and temp_obj >= TEMP_ALERTA:
        enviar_emergencia()
    else:
        if temp_obj >= TEMP_ALERTA:
            enviar_emergencia()

# Conectar inicialmente
conectar_mqtt()

# Bucle principal
try:
    while True:
        enviar_datos_periodicos()
        time.sleep(5)
        
except KeyboardInterrupt:
    print("Deteniendo sistema...")
    client.disconnect()