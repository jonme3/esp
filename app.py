from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Variable de estado para el ESP32 (simula el estado del dispositivo)
esp32_connected = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estado')
def estado():
    # Devuelve el estado del ESP32 en formato JSON
    return jsonify(status="Conectado" if esp32_connected else "Desconectado")

# Endpoint para simular que el ESP32 se conecta después de 10 segundos
@app.route('/conectar')
def conectar():
    global esp32_connected
    esp32_connected = True
    return "ESP32 conectado", 200

if __name__ == '__main__':
    app.run(debug=True)
