
# DOCUMENTATION DE L'APPLICATION FLASK
"""
    Description de l'application Flask:
    
    Ceci est une application Flask qui expose une API REST permettant d'exécuter des scripts Python et de retourner leur sortie sous forme de chaîne de caractères JSON. 
    
    L'API peut être accédée en utilisant trois méthodes HTTP : POST, GET et PUT.

    La fonction create_script exécute le script spécifié lorsqu'elle est accédée via une requête POST et retourne une représentation en chaîne de caractères JSON de la sortie du script. 
    
    La fonction get_script retourne la même représentation en chaîne de caractères JSON de la sortie du script lorsqu'elle est accédée via une requête GET. 
    
    La fonction update_script exécute le script spécifié lorsqu'elle est accédée via une requête PUT et retourne une représentation en chaîne de caractères JSON de la sortie du script.

    La sortie du script doit être un dictionnaire Python, sinon un message d'erreur sera retourné. 
    
    La fonction get_ip_address du module info_server est importée et utilisée dans les trois fonctions pour récupérer l'adresse IP du serveur.
"""

# Import des différents modules Python
import subprocess
import ast
import json

# Import des modules Flask 
from flask import Flask, render_template, request, jsonify

# Ajoutez le chemin vers le dossier Application
import sys
sys.path.append('Application')
# On ajoute le chemin vers le dossier Application pour qu'on puisse importer nos modules

# Importe de nos modules Python personnalisés
from modules.info_server import get_ip_address as ip_address


# Création de l'application Flask
app = Flask(__name__, template_folder='template')

# Définition d'une route qui accepte les méthodes POST
@app.route('/api/<script>', methods=['POST'])
def create_script(script):
    # Récupération des données envoyées en PUT dans une variable 'data'
    data = request.get_json()
    
    # Récupération du nom du script à exécuter dans la variable 'script'
    script = data['script']
    
    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(['python', f'Application/modules/{script}'], stdout=subprocess.PIPE)
    
    # Récupération de la sortie standard du script exécuté
    output = result.stdout.decode('utf-8')
    
    # Conversion de la sortie du script en un dictionnaire Python
    result_script = ast.literal_eval(output)
    
    # Si la liste est vide ou que ce n'est pas un dictionnaire, on retourne un message d'erreur
    if result_script is None or not isinstance(result_script, dict):
        return "Aucune information sur le serveur disponible"
    
    # Conversion du dictionnaire en une chaîne de caractères au format JSON
    result_script_json = json.dumps(result_script)
    
    # Retour de la chaîne de caractères au format JSON avec l'en-tête 'Content-Type: application/json'
    return jsonify(resultresult_script_json=result_script_json)

# Définition d'une route qui accepte les méthodes GET
@app.route('/api/<script>', methods=['GET'])
def get_script(script):
    # Récupération des données envoyées en PUT dans une variable 'data'
    data = request.get_json()
    
    # Récupération du nom du script à exécuter dans la variable 'script'
    script = data['script']
    
    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(['python', f'Application/modules/{script}'], stdout=subprocess.PIPE)
    
    # Récupération de la sortie standard du script exécuté
    output = result.stdout.decode('utf-8')
    
    # Conversion de la sortie du script en un dictionnaire Python
    result_script = ast.literal_eval(output)
    
    # Si la liste est vide ou que ce n'est pas un dictionnaire, on retourne un message d'erreur
    if result_script is None or not isinstance(result_script, dict):
        return "Aucune information sur le serveur disponible"
    
    # Conversion du dictionnaire en une chaîne de caractères au format JSON
    result_script_json = json.dumps(result_script)
    
    # Retour de la chaîne de caractères au format JSON avec l'en-tête 'Content-Type: application/json'
    return jsonify(resultresult_script_json=result_script_json)

# Définition d'une route qui accepte les méthodes PUT
@app.route('/api/<script>', methods=['PUT'])
def update_script(script):
    # Récupération des données envoyées en PUT dans une variable 'data'
    data = request.get_json()
    
    # Récupération du nom du script à exécuter dans la variable 'script'
    script = data['script']
    
    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(['python', f'Application/modules/{script}'], stdout=subprocess.PIPE)
    
    # Récupération de la sortie standard du script exécuté
    output = result.stdout.decode('utf-8')
    
    # Conversion de la sortie du script en un dictionnaire Python
    result_script = ast.literal_eval(output)
    
    # Si la liste est vide ou que ce n'est pas un dictionnaire, on retourne un message d'erreur
    if result_script is None or not isinstance(result_script, dict):
        return "Aucune information sur le serveur disponible"
    
    # Conversion du dictionnaire en une chaîne de caractères au format JSON
    result_script_json = json.dumps(result_script)
    
    # Retour de la chaîne de caractères au format JSON avec l'en-tête 'Content-Type: application/json'
    return jsonify(resultresult_script_json=result_script_json)

# Définition d'une route qui accepte les méthodes GET
@app.route('/api/test')
def execute_script():
    # Exécution du script 'info_server.py' et récupération du dictionnaire de résultat
    result = subprocess.run(['python', 'Application/modules/info_server.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    info_server = liste
    
    # Si le dictionnaire est vide, on retourne un message d'erreur

    if info_server is None or not isinstance(info_server, dict):
        return "Aucune information sur le serveur disponible"
    
    
    # Utilisez la fonction render_template de Jinja2 pour afficher le résultat en HTML
    return render_template('info_server.html', info_server=info_server.items())

@app.route('/')
def index():
    
    return render_template('index.html')

if __name__ == '__main__':
    # on récupère l'adresse IP de la machine
    ip = ip_address()
    # on lance l'application Flask avec le mode debug activé et sur l'adresse IP de la machine ainsi que sur le port donnée
    app.run(host=ip,port=5600,debug=True)

