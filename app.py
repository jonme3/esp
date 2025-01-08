from flask import Flask, jsonify, request, render_template

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
    global esp32_connected
    # Recibimos la solicitud del ESP32 y actualizamos el estado de la conexión
    data = request.get_json()
    if data and data.get("status") == "Conectado":
        esp32_connected = True
    return jsonify(message="Estado actualizado"), 200

if __name__ == '__main__':
    app.run(debug=True)
