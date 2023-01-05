import subprocess
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/run_script', methods=['POST'])
def run_script():
    # Récupérez les données de la requête HTTP (par exemple, le nom du script à exécuter et les arguments à passer)
    data = requests.get_json()
    script_name = data['script_name']

    # Exécutez le script en utilisant la commande subprocess.run
    result = subprocess.run(['python', script_name])

    # Récupérez les résultats du script et stockez-les dans une variable
    script_results = result.stdout

    # Renvoyez les résultats du script au serveur
    return {'results': script_results}

@app.route('/test_results')
def test_results():
    # Exécutez votre script de test en utilisant la commande subprocess.run
    result = subprocess.run(['python', 'Application/modules/info_server.py'])
    # Récupérez les résultats de votre script et stockez-les dans une variable (par exemple, 'results')
    results = result.stdout
    return results

if __name__ == '__main__':
    app.run(host="localhost",port=5600,debug=True)