import streamlit as st
from flask import Flask, request
from threading import Thread

# Crear una aplicación Flask para manejar las solicitudes HTTP
app = Flask(__name__)

# Definir la ruta para manejar las solicitudes GET
@app.route('/esp32', methods=['GET'])
def esp32_connection():
    # Cuando se reciba la solicitud GET del ESP32, actualizamos la página de Streamlit
    return "Conectado al ESP32 correctamente"

# Función para ejecutar Flask en un hilo separado
def run_flask():
    app.run(host="0.0.0.0", port=5000, debug=False)

# Crear una interfaz en Streamlit
st.title('Interfaz para ESP32')
st.write("Esperando conexión desde el ESP32...")

# Usamos un hilo para ejecutar Flask y mantener Streamlit activo
thread = Thread(target=run_flask)
thread.start()

# Mostrar un mensaje cuando el ESP32 se haya conectado
st.write("¡El ESP32 está conectado!")
