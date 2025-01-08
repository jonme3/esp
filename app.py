from flask import Flask, render_template, jsonify
from flask_cors import CORS

# Inicializa la aplicación Flask y CORS para permitir solicitudes de otros orígenes
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/conectar', methods=['POST'])
def conectar():
    # Aquí procesamos la solicitud POST que recibe el ESP32
    return jsonify({"status": "success", "message": "Conectado al ESP32"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
