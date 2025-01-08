from flask import Flask, request, jsonify
from flask_cors import CORS  # Importamos para manejar CORS si es necesario

app = Flask(__name__)
CORS(app)  # Permitir CORS para que pueda recibir solicitudes desde otras fuentes

@app.route('/')
def index():
    return '¡Bienvenido a la página principal!'

@app.route('/conectar', methods=['POST'])
def conectar():
    data = request.get_json()  # Obtener los datos enviados desde el ESP32
    esp_id = data.get('esp_id', 'Desconocido')

    print(f"Conexión recibida desde: {esp_id}")  # Mostrar el ID del ESP32

    # Responder al ESP32 con un mensaje indicando que está conectado
    return jsonify({"status": "success", "message": f"Conectado a {esp_id}"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
