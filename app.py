from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de que index.html esté en la carpeta correcta

@app.route('/conectar', methods=['POST'])
def conectar():
    # Verifica si el ESP32 está realmente conectado
    # Esto es solo un ejemplo, puedes hacer una verificación adicional si tienes alguna forma de hacerlo
    current_time = time.time()
    
    # Simula la verificación de conexión con un tiempo de respuesta
    if current_time % 2 == 0:  # Justo por ejemplo, responde solo en momentos específicos
        return jsonify({"status": "success", "message": "Conectado al ESP32"}), 200
    else:
        return jsonify({"status": "error", "message": "No hay conexión con el ESP32"}), 404

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
