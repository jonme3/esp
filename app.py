import time
import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Cambia esta URL por la del ESP32
ESP32_URL = 'http://<esp32_ip>/status'  # Asegúrate de que el ESP32 tenga una ruta de este tipo

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estado', methods=['GET'])
def estado():
    try:
        # Intentar hacer un ping al ESP32
        response = requests.get(ESP32_URL, timeout=5)  # Tiempo máximo de espera de 5 segundos
        if response.status_code == 200:
            return jsonify({"status": "success", "message": "Conectado al ESP32"}), 200
        else:
            return jsonify({"status": "error", "message": "No hay conexión con el ESP32"}), 404
    except requests.exceptions.RequestException:
        # Si no hay respuesta o algún error, asumimos que está desconectado
        return jsonify({"status": "error", "message": "No hay conexión con el ESP32"}), 404

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
