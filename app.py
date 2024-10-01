from flask import Flask, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/executar_script', methods=['GET'])
def executar_script():
    resultado = "Olá, mundo!"
    return jsonify(resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
