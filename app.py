from flask import Flask, render_template, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de que index.html esté en la carpeta correcta

@app.route('/conectar', methods=['POST'])
def conectar():
    # Aquí, el ESP32 hace la solicitud POST
    print("ESP32 conectado")  # Esto es solo para fines de depuración
    return jsonify({"status": "success", "message": "Conectado al ESP32"}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
