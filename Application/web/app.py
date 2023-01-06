import subprocess
from flask import Flask, render_template, request, jsonify
import sys
sys.path.append('Application')
from modules.info_server import get_ip_address as ip_address
import ast
import json

app = Flask(__name__, template_folder='template')

@app.route('/api/<script>', methods=['POST'])
def create_script(script):
    data = request.get_json()
    script = data['script']
    result = subprocess.run(['python', f'Application/modules/{script}'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    if liste is None or not isinstance(liste, dict):
        return "Aucune information sur le serveur disponible"
    json_string = json.dumps(liste)
    return jsonify(result=json_string)

@app.route('/api/<script>', methods=['GET'])
def get_script(script):
    data = request.get_json()
    script = data['script']
    result = subprocess.run(['python', f'Application/modules/{script}'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    if liste is None or not isinstance(liste, dict):
        return "Aucune information sur le serveur disponible"
    json_string = json.dumps(liste)
    return jsonify(result=json_string)


@app.route('/api/<script>', methods=['PUT'])
def update_script(script):
    data = request.get_json()
    script = data['script']
    result = subprocess.run(['python', f'Application/modules/{script}'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    if liste is None or not isinstance(liste, dict):
        return "Aucune information sur le serveur disponible"
    
    json_string = json.dumps(liste)
    return jsonify(result=json_string)


@app.route('/api/test')
def execute_script():
    # Exécutez le script et récupérez le dictionnaire de résultat
    result = subprocess.run(['python', 'Application/modules/info_server.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    info_server = liste
    
    if info_server is None or not isinstance(info_server, dict):
        return "Aucune information sur le serveur disponible"
    
    
    # Utilisez la fonction render_template de Jinja2 pour afficher le résultat en HTML
    return render_template('info_server.html', info_server=info_server.items())


if __name__ == '__main__':
    ip = ip_address()
    app.run(host=ip,port=5600,debug=True)