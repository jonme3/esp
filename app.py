from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Variable global para almacenar el estado de la entrada
estado_actual = 0

# Endpoint para manejar la conexión y recibir el estado
@app.route('/conectar', methods=['POST'])
def conectar():
    global estado_actual
    # Asegúrate de que los datos sean recibidos en formato JSON
    data = request.json
    if 'estado' in data:
        estado_actual = data['estado']  # Actualiza el estado con los datos recibidos
        return jsonify({"message": "Estado recibido", "estado": estado_actual}), 200
    return jsonify({"error": "Datos no válidos"}), 400

# Endpoint para obtener el estado actual
@app.route('/estado', methods=['GET'])
def obtener_estado():
    return jsonify({"estado": estado_actual})

# Ruta principal para servir el HTML (index.html)
@app.route('/')
def index():
    return render_template('index.html')  # Asegúrate de tener el archivo 'index.html' en la carpeta 'templates'

# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
