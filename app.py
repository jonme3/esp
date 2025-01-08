from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Esperando conexión..."  # Puedes devolver algo más específico si deseas.

@app.route('/esp32_connected', methods=['GET'])
def esp32_connected():
    return jsonify({"status": "Conectado"}), 200  # Respuesta a la conexión del ESP32

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
