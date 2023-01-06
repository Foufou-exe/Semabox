import subprocess
from flask import Flask, render_template, request, jsonify
import sys
sys.path.append('Application')
from modules.info_server import get_ip_address as ip_address
import ast

app = Flask(__name__, template_folder='template')

@app.route('/api/<script>', methods=['POST'])
def create_script(script):
    script = request.get_json()['script']
    result = execute_script(f'Application/modules/{script}')
    return jsonify(result=result)

@app.route('/api/<script>', methods=['GET'])
def get_script(script):
    # récupérez le nom du script
    script = request.get_json()['script']
    result = execute_script(f'Application/modules/{script}')
    return jsonify(result=result)

@app.route('/api/<script>', methods=['PUT'])
def update_script(script):
    script = request.get_json()[f'Application/modules/{script}']
    result = execute_script(script)
    return jsonify(result=result)


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