from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Servir el archivo HTML cuando se acceda a la raíz

@app.route('/esp32_connected', methods=['GET'])
def esp32_connected():
    # Aquí estamos respondiendo a las solicitudes del ESP32
    return jsonify({"status": "Conectado"}), 200  # Responder que el ESP32 está conectado

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
