
![sketch-1742284216881](https://github.com/user-attachments/assets/d89cfb6f-bccc-457d-9c45-467bbb633261)

# Información estudiantes y cooevaluaciones

## Información de Integrantes

| Nombre                               | Gerardo Manzano Villafaña     | Celeste Estefanía Ramírez Matehuala |
|--------------------------------------|-------------------------------|-------------------------------------|
| Número de control                    | 1222100474                    | 1223100435                           |
| Grupo                                | GDS0652                       | GDS0652                              |


## Parte Socioafectiva

### Comentarios de Evaluación

#### Gerardo Manzano Villafaña

| Aspecto             | Comentario                                                                                                       |
|---------------------|------------------------------------------------------------------------------------------------------------------|
| **Positivo**        | En una persona que siempre está dispuesta a ayudar, está en completa disposición de siempre ofrecerse para ayudar cuando el trabajo en equipo lo requiera. Es amable y cooperativo incluso en las compras de material. Es un excelente compañero, muy comprensivo y paciente|
| **Negativo**        | Requiere practicar un poco más su programación. Y también debe de dejar de subestimarse, tiene excelentes habilidades pero no es capaz de reconocerlas|
| **A mejorar**       | Puede mejorar su comunicación, y sus habilidades técnicas.|

#### Celeste Estefanía Ramírez Matehuala

| Aspecto             | Comentario                                                                                                         |
|---------------------|--------------------------------------------------------------------------------------------------------------------|
| **Positivo**        | Es una persona muy disciplinada y cumplida, tiene un enfoque directo y es difícil distraerla de sus objetivos, por lo cual resulta una compañera perfecta para realizar el trabajo en equipo. Aporta información e imparte su conocimiento para la constante mejora del equipo, es amable y paciente. |
| **Negativo**        | Suele estresarse por ciertas cuestiones y en esos casos se bloquea en la búsqueda de una solución temporal.|
| **A mejorar**       | Se puede mejorar la comunicación.|




![sketch-1742284216881](https://github.com/user-attachments/assets/cdc90bef-f17a-427a-adac-4304b3c4390f)



# 🚒 FIRE-ALARM: Sistema de Alarma de Incendios

## 📖 Descripción General
FIRE-ALARM es un sistema de alarma de incendios basado en un microcontrolador ESP32 y Node-RED para la detección temprana de humo y temperatura elevada. Envía señales sonoras y visuales, registra datos en una base de datos local (SQLite) y permite monitoreo remoto desde una interfaz web.

## 🎯 Objetivos del Proyecto
- Detectar humo y temperatura anómala para alertar de posibles incendios.
- Generar alarma sonora y visual (buzzer y LEDs).
- Registrar eventos y valores de sensor en una base de datos.
- Proporcionar una interfaz web con Node-RED para monitoreo y notificaciones.

# Elementos

## ⚙️ Tecnologías Utilizadas

| Tecnología      | Uso Principal                                     | Imagen |
|-----------------|---------------------------------------------------|  |
| **ESP32**       | Lectura de sensores y control de actuadores       | ![image](https://github.com/user-attachments/assets/9d24e5f8-f32d-4ce6-82b6-b8c6cbef06ea)
 |
| **Node‑RED**    | Orquestación de flujos y panel de control web     | ![image](https://github.com/user-attachments/assets/2325d672-f5dc-4d93-b74a-073e0d5135c4)
 |
| **SQLite**      | Almacenamiento local de registros de eventos      |![image](https://github.com/user-attachments/assets/0394a3c9-e3cf-49a1-bf13-f1cbefddf59d)
  |
| **MQTT**        | Comunicación entre ESP32 y Node‑RED               | ![image](https://github.com/user-attachments/assets/7fad99c4-ef89-4028-92c0-ff252085b273)
 |
| **3D Printing** | Carcasa y soportes para sensores y actuadores     | ![image](https://github.com/user-attachments/assets/cfe79854-92ac-4927-9fae-e7fef90d7944)
 |


## Tabla de materiales 

| Nombre | Función | Precio | Imagen |
|------------------------------------|--------|--------|--------------|
| **Buzzer Pasivo** | Sirve para poder generar un sonido tras recibir una señal, de estos se adquirieron 2 | $60.00 | ![image](https://github.com/user-attachments/assets/a5794c70-3558-4381-9c8e-f1f7f7208288)
      |
| **Tira led** | Sirve para marcar el color del estado en el que se encuentra el sistema | $20.00 |![image](https://github.com/user-attachments/assets/f4dc5553-1a82-49e0-9a13-11296590232d)|
| **Led** | Sirve para marcar el color del estado en el que se encuentra el sistema | $10.00 |![image](https://github.com/user-attachments/assets/517844dc-1c3c-4004-a811-e6621f91916d)
|
| **Carcasa** | Estructura física del sistema | $180.00 | |
| **Carcasa** | Sirve para marcar el color del estado en el que se encuentra el sistema | $180.00 ||

## Tabla de sensores

| Nombre | Función | Precio | Imagen |
|------------------------------------|--------|--------|--------|
| **Módulo Termómetro Infrarrojo Mlx90614, Electrónica, Arduino** | Detecta por infrarojo la temperatura ambiente y de un objeto | $350.00 | ![image](https://github.com/user-attachments/assets/ee0894b2-f692-44b0-a09a-756c06af1f28)
 |
| **MQ-2** | Detecta la sensidad del aire y sirve para verificar si hay humo | $50.00|![image](https://github.com/user-attachments/assets/e3583f5a-6d15-42b0-abfd-6d0f22655b1a)
  |
| **Modulo Pir Hc-sr501 Sensor Presencia Movimiento Infrarrojo** | Detecta el movimiento | $50.00 | ![image](https://github.com/user-attachments/assets/d732be06-a304-4d6b-98ee-f2cd6874ce01)
 |




