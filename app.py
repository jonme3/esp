from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Variable global para almacenar el estado de la entrada
estado_actual = 0

@app.route('/conectar', methods=['POST'])
def conectar():
    global estado_actual
    data = request.json  # Obtener datos en formato JSON
    if 'estado' in data:
        estado_actual = data['estado']
        return jsonify({"message": "Estado recibido", "estado": estado_actual}), 200
    return jsonify({"error": "Datos no válidos"}), 400

@app.route('/estado', methods=['GET'])
def obtener_estado():
    return jsonify({"estado": estado_actual})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
