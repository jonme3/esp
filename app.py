from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

# Variable global para guardar el estado de la conexión del ESP32
esp32_connected = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estado')
def estado():
    # Devuelve el estado actual de la conexión del ESP32
    return jsonify(status="Conectado" if esp32_connected else "Desconectado")

@app.route('/conectar', methods=['POST'])
def conectar():
    data = request.get_json()
    if data and data.get("status") == "Conectado":
        esp32_connected = True
        print("ESP32 está conectado.")
        return jsonify(message="Conectado", status="success"), 200
    else:
        return jsonify(message="No conectado", status="fail"), 400
        
if __name__ == '__main__':
    # Obtiene el puerto de la variable de entorno
    port = int(os.environ.get("PORT", 5000))  # Usa el puerto proporcionado por Render o 5000 por defecto
    app.run(host="0.0.0.0", port=port, debug=True)  # Asegúrate de que Flask escuche en todas las interfaces (0.0.0.0)
