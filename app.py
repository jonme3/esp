from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite las solicitudes CORS desde cualquier origen

esp32_connected = False

@app.route('/')
def index():
    return "¡Bienvenido a la página principal!"

@app.route('/conectar', methods=['POST'])
def conectar():
    global esp32_connected

    # Obtén los datos enviados por el ESP32
    data = request.get_json()

    if data['status'] == 'success':
        esp32_connected = True
        print("ESP32 conectado:", data['message'])
        return jsonify({"status": "success", "message": "Conectado al ESP32"}), 200
    else:
        esp32_connected = False
        return jsonify({"status": "error", "message": "No hay conexión con el ESP32"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
