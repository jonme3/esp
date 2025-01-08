from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  # Para permitir CORS si se necesita

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Sirve la página index.html

@app.route('/conectar', methods=['POST'])
def conectar():
    data = request.get_json()  # Obtiene los datos enviados desde el ESP32
    esp_id = data.get('esp_id', 'Desconocido')  # Obtiene el ID del ESP32, si está presente

    print(f"Conexión recibida desde: {esp_id}")  # Muestra en la consola el ID del ESP32

    # Responder con un mensaje indicando que se conectó correctamente
    return jsonify({"status": "success", "message": f"Conectado a {esp_id}"}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
