import subprocess
import requests
from flask import Flask , request, jsonify
import sys
sys.path.append('Application')
from modules.info_server import get_ip_address as ip_address

app = Flask(__name__)

# @app.route('/run_script', methods=['POST'])
# def run_script():
#     # Récupérez les données de la requête HTTP (par exemple, le nom du script à exécuter et les arguments à passer)
#     data = requests.get_json()
#     script_name = data['script_name']

#     # Exécutez le script en utilisant la commande subprocess.run
#     result = subprocess.run(['python', f'modules/{script_name}'])

#     # Récupérez les résultats du script et stockez-les dans une variable
#     script_results = result.stdout

#     # Renvoyez les résultats du script au serveur
#     return {'results': script_results}

# @app.route('/test_results')
# def test_results():
#     # Exécutez votre script de test en utilisant la commande subprocess.run
#     result = subprocess.run(['python', 'modules/info_server.py'])
#     # Récupérez les résultats de votre script et stockez-les dans une variable (par exemple, 'results')
#     results = result.stdout
#     return results

@app.route('/api/scripts', methods=['POST'])
def create_script():
    script = request.get_json()['script']
    result = execute_script(f'modules/{script}')
    return jsonify(result=result)

@app.route('/api/scripts', methods=['GET'])
def get_script(script):
    # récupérez le nom du script 
    result = execute_script(f'modules/{script}')
    return jsonify(result=result)

@app.route('/api/scripts', methods=['PUT'])
def update_script(script):
    script = request.get_json()[f'modules/{script}']
    result = execute_script(script)
    return jsonify(result=result)

@app.route('/api/test')
def execute_script():
    result = subprocess.run(['python', 'Application/modules/info_server.py'])
    return "<html><body><pre>{}</pre></body></html>".format(result)




if __name__ == '__main__':
    ip = ip_address()
    app.run(host=ip,port=5600,debug=True)