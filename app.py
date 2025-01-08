from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Para permitir las solicitudes CORS desde otro dominio

app = Flask(__name__)
CORS(app)

# Variable global para almacenar el estado de la conexión
esp_connected = False  # Inicialmente, el ESP32 no está conectado

@app.route('/')
def index():
    return render_template('index.html')  # Sirve la página principal

@app.route('/conectar', methods=['POST'])
def conectar():
    global esp_connected
    data = request.get_json()  # Recibe los datos enviados desde el ESP32
    esp_id = data.get('esp_id', 'Desconocido')  # Obtiene el ID del dispositivo ESP32

    # Simulamos una lógica para cambiar el estado de conexión
    if esp_id == "ESP32_12345":
        esp_connected = True  # Cambia el estado de conexión si el ID es correcto
    else:
        esp_connected = False  # Si el ID no es correcto, considera que está desconectado

    # Responde con el estado de la conexión
    if esp_connected:
        return jsonify({"status": "success", "message": f"Conectado a {esp_id}"}), 200
    else:
        return jsonify({"status": "error", "message": "No hay conexión con el ESP32"}), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
