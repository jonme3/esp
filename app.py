from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# Ruta principal que muestra una página HTML
@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de tener este archivo HTML

# Evento que escucha cuando el ESP32 se conecta
@socketio.on('esp_connected')
def handle_esp_connection(data):
    print('ESP32 Conectado:', data)
    emit('server_response', {'message': '¡ESP32 Conectado!'})

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
