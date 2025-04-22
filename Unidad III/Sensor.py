from machine import Pin, ADC
from time import sleep
import urequests
import network

# Configurar sensor KY-036
pin_analogico = ADC(Pin(34))  # Entrada analógica en GPIO 34
pin_analogico.atten(ADC.ATTN_11DB)  # Rango completo (0-3.3V, 0-4095)

pin_digital = Pin(14, Pin.IN)  # Entrada digital en GPIO 14

# Configurar WiFi
def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect("celeste", "12345678")
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.5)
    print("\nWiFi OK IP:", sta_if.ifconfig()[0])

connect_wifi()

# URL de Google Sheets (WebApp)
WEBAPP_URL = ""

def send_to_sheets(digital_value, analog_value):
    data = {
        "digital": digital_value,
        "analogico": analog_value,
    }
    try:
        response = urequests.post(WEBAPP_URL, json=data)
        print("Respuesta:", response.text)
        response.close()
    except Exception as e:
        print("Error enviando datos:", e)

while True:
    try:
        # Leer valores del sensor
        analogico = pin_analogico.read()  # Valor de 0 a 4095
        digital = pin_digital.value()  # 0 o 1

        # Imprimir valores en consola
        print(f"Valor Analógico: {analogico}")
        print(f"Valor Digital: {digital}")
        print("-" * 20)

        # Enviar datos a Google Sheets
        send_to_sheets(digital, analogico)

    except Exception as e:
        print("Error al leer sensor:", e)
    sleep(2)
