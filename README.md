
![sketch-1742284216881](https://github.com/user-attachments/assets/d89cfb6f-bccc-457d-9c45-467bbb633261)

---

# 📋 Información de Estudiantes y Cooevaluaciones

## 👥 Integrantes

| Nombre                              | Núm. de Control | Grupo   |
|-------------------------------------|-----------------|---------|
| **Gerardo Manzano Villafaña**       | 1222100474      | GDS0652 |
| **Celeste E. Ramírez Matehuala**    | 1223100435      | GDS0652 |

## 💬 Parte Socioafectiva

### Gerardo Manzano Villafaña

| Aspecto       | Comentario                                                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Positivo**  | Siempre dispuesto a ayudar; amable y cooperativo incluso en compras de material; excelente compañero, comprensivo y paciente.                     |
| **Negativo**  | Debe practicar más su programación y dejar de subestimarse.                                                                                      |
| **A mejorar** | Comunicación y habilidades técnicas.                                                                                                            |

### Celeste E. Ramírez Matehuala

| Aspecto       | Comentario                                                                                                                                       |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| **Positivo**  | Muy disciplinada y cumplida; enfoque directo; aporta conocimiento; amable y paciente.                                                           |
| **Negativo**  | Se estresa en ciertas situaciones y puede bloquearse buscando soluciones.                                                                       |
| **A mejorar** | Comunicación.                                                                                                                                    |

---

# 🚒 FIRE‑ALARM: Sistema de Alarma de Incendios

## 📖 Descripción General
FIRE‑ALARM es un sistema de alarma de incendios basado en ESP32 y Node‑RED. Detecta humo y temperatura elevada, emite alertas sonoras y visuales, registra eventos en SQLite y ofrece monitoreo remoto vía interfaz web.

## 🎯 Objetivos
- Detectar humo y temperatura anómala.  
- Generar alarma sonora (buzzer) y visual (LEDs).  
- Registrar eventos en base de datos local.  
- Monitoreo y notificaciones a través de Node‑RED.

---

## ⚙️ Tecnologías Utilizadas

| Tecnología     | Uso                                       | Imagen                                                                                                                          |
|----------------|-------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| **ESP32**      | Lectura de sensores y control de actuadores | <img src="https://github.com/user-attachments/assets/9d24e5f8-f32d-4ce6-82b6-b8c6cbef06ea" width="150" height="150" alt="ESP32"/> |
| **Node‑RED**   | Orquestación de flujos y dashboard web    | <img src="https://github.com/user-attachments/assets/2325d672-f5dc-4d93-b74a-073e0d5135c4" width="150" height="150" alt="Node‑RED"/> |
| **SQLite**     | Almacenamiento de registros               | <img src="https://github.com/user-attachments/assets/0394a3c9-e3cf-49a1-bf13-f1cbefddf59d" width="150" height="150" alt="SQLite"/>   |
| **MQTT**       | Comunicación entre ESP32 y Node‑RED       | <img src="https://github.com/user-attachments/assets/7fad99c4-ef89-4028-92c0-ff252085b273" width="150" height="150" alt="MQTT"/>    |
| **3D Printing**| Carcasa y soportes para sensores y actuadores | <img src="https://github.com/user-attachments/assets/cfe79854-92ac-4927-9fae-e7fef90d7944" width="150" height="150" alt="3D Printing"/> |

---

## 📦 Materiales

| Nombre            | Función                                          | Precio   | Imagen                                                                                                                             |
|-------------------|--------------------------------------------------|----------|------------------------------------------------------------------------------------------------------------------------------------|
| **Buzzer Pasivo** | Genera sonido de alarma (×2 unidades)            | \$60.00  | <img src="https://github.com/user-attachments/assets/a5794c70-3558-4381-9c8e-f1f7f7208288" width="150" height="150" alt="Buzzer"/>  |
| **Tira LED**      | Indica estado con color                          | \$20.00  | <img src="https://github.com/user-attachments/assets/f4dc5553-1a82-49e0-9a13-11296590232d" width="150" height="150" alt="Tira LED"/> |
| **LED**           | Señalización visual (×3 unidades)                | \$10.00  | <img src="https://github.com/user-attachments/assets/517844dc-1c3c-4004-a811-e6621f91916d" width="150" height="150" alt="LED"/>     |
| **Carcasa 3D**    | Estructura física del sistema                    | \$180.00 |                                                                                                                                     |

---

## 🌡️ Sensores

| Nombre                                          | Función                                                       | Precio   | Imagen                                                                                                                               |
|-------------------------------------------------|---------------------------------------------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------|
| **Termómetro IR MLX90614**                     | Mide temperatura sin contacto                                | \$350.00 | <img src="https://github.com/user-attachments/assets/ee0894b2-f692-44b0-a09a-756c06af1f28" width="150" height="150" alt="MLX90614"/> |
| **Detector de Humo MQ-2**                       | Detecta concentración de gas y humo                           | \$50.00  | <img src="https://github.com/user-attachments/assets/e3583f5a-6d15-42b0-abfd-6d0f22655b1a" width="150" height="150" alt="MQ-2"/>         |
| **Sensor PIR HC-SR501**                         | Detecta movimiento                                            | \$50.00  | <img src="https://github.com/user-attachments/assets/d732be06-a304-4d6b-98ee-f2cd6874ce01" width="150" height="150" alt="PIR"/>          |

---

# Diagramas de conexión

| Nombre | Descripción | Diagrama  |
|------|-----|------|
| **Diagrama del circuito** | Diagrama de conexión de los sensores y actuadores, es se representan los que están dentro de la carcasa | ![circuit_image (4)](https://github.com/user-attachments/assets/c932c7ba-e8cb-4f68-8894-e918a90969a8) |
| **Diagrama de la bomba** | Diagrama de conexión de la bomba de agua que se da tras la alarma | ![Imagen de WhatsApp 2025-04-21 a las 17 27 29_78030dbc](https://github.com/user-attachments/assets/601de88d-396b-4f49-a398-99b6cde42f73) |

---

# 🔥 Sistema de Monitoreo y Alerta de Incendios – Interfaz Gráfica

Este sistema fue desarrollado utilizando **Node-RED** como plataforma principal para la creación de una interfaz gráfica interactiva y visualmente organizada, permitiendo el control, supervisión y análisis de los eventos del sistema.

## 🧩 Funcionalidades de la Interfaz

- ✅ **Activación manual de la alarma** desde el dashboard mediante un interruptor interactivo, accesible desde cualquier navegador.
- 📊 **Gráfica de promedio de temperaturas** (ambiente y objeto) calculado con base en los últimos registros almacenados en SQLite.
- 📈 **Promedio global de densidad** de humo/gas, con análisis visual del estado del aire registrado por los sensores.
- 📊 **Frecuencia de estados de densidad**, diferenciando condiciones como `poco_adecuada`, `adecuada`, etc.
- 🚶 **Gráfico de estados de movimiento**, permitiendo visualizar cuántas veces se ha detectado presencia.
- 🚨 **Gráficas de alertas**:
  - Por **tipo de alerta** (e.g., activación manual, detección de incendio).
  - Por **severidad** (e.g., advertencia, peligrosa).
- 📬 **Notificaciones automáticas por correo electrónico** a los encargados registrados, ante cada evento de emergencia.
- 👥 **Formulario de registro de encargados**, con validación para evitar duplicados y almacenamiento de nombre, correo y fecha de registro.
- 🧠 **Dashboard limpio y organizado por pestañas**, cada una dedicada a un componente específico del sistema (temperatura, densidad, movimiento, alertas).

![image](https://github.com/user-attachments/assets/e66bcb33-c9c4-4c48-abaf-a70f408d92b9)
![image](https://github.com/user-attachments/assets/41872908-8c09-411f-b045-539ec0a2e392)



## 💾 Base de Datos

Toda la información se almacena en una base de datos local SQLite (`firealarm.db`), organizada en tablas como:

- `registro_temperaturas`
- `registro_densidad`
- `registro_movimiento`
- `registro_alertas`
- `encargados`

## 🚀 Tecnologías Utilizadas

- Node-RED
- MQTT (Mosquitto)
- SQLite
- Gmail SMTP (para envío de correos)

---

Este sistema proporciona una solución completa para monitoreo ambiental, detección de incendios y alertas en tiempo real, ideal para entornos escolares, industriales o domésticos.

---

# Video de la funcionabilidad

![image](https://github.com/user-attachments/assets/3ca707f7-db00-4779-b7cd-35b3d635e6b6)


