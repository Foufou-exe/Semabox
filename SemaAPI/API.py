
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

"""
    Description de la Librairie Flask:
        Les modules Flask :
            Flask = Framework Python pour créer des applications Web  
            request = module qui permet de récupérer les données envoyées dans une requête HTTP
            jsonify = module qui permet de convertir un dictionnaire Python en une chaîne de caractères JSON
            abort = module qui permet de retourner une erreur HTTP
"""


from flask import Flask, render_template, jsonify, abort, Response, request, session

# Ajoutez le chemin vers le dossier Semabox/SemaOS
import sys
sys.path.append('./SemaOS')
# On ajoute le chemin vers le dossier Semabox/SemaOS pour qu'on puisse importer nos modules

# Importe de nos modules Python personnalisés
from info_server import get_ip_address as ip
from scan_servers import api_scan_nmap 

# Création de l'application Flask
app = Flask(__name__, template_folder='template')
app.secret_key = "./SemaAPI/secret_key"

# Définition d'une route qui accepte les méthodes POST
@app.route('/api/<script>', methods=['POST'])
def create_script(script):
    
    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(['python', f'./SemaOS/{script}'], stdout=subprocess.PIPE)
    
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
    return jsonify(result_script_json=result_script_json)

# Définition d'une route qui accepte les méthodes GET
@app.route('/api/<script>', methods=['GET'])
def get_script(script):
    
    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(['python', f'./SemaOS/{script}'], stdout=subprocess.PIPE)
    
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
    return jsonify(result_script_json=result_script_json)

# Définition d'une route qui accepte les méthodes PUT
@app.route('/api/<script>', methods=['PUT'])
def update_script(script):
    
    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(['python', f'./SemaOS/{script}'], stdout=subprocess.PIPE)
    print(result.stdout)
    # Récupération de la sortie standard du script exécuté
    output = result.stdout.decode('utf-8')
    
    # Conversion de la sortie du script en un dictionnaire Python
    result_script = ast.literal_eval(output)
    
    # Si la liste est vide ou que ce n'est pas un dictionnaire, on retourne un message d'erreur
    if result_script is None or not isinstance(result_script, dict):
        abort(404, "Aucune information sur le serveur disponible")
    
    
    
    # Conversion du dictionnaire en une chaîne de caractères au format JSON
    result_script_json = json.dumps(result_script)
    
    # Retour de la chaîne de caractères au format JSON avec l'en-tête 'Content-Type: application/json'
    return jsonify(resultresult_script_json=result_script_json)

# Définition d'une route qui accepte les méthodes GET
@app.route('/api/test')
def execute_script():
    # Exécution du script 'info_server.py' et récupération du dictionnaire de résultat
    result = subprocess.run(['python', './SemaOS/info_server.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    info_server = liste
    
   # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if info_server is None or not isinstance(info_server, dict):
        return "Aucune information sur le serveur disponible"
    
    
    # Utilisez la fonction render_template de Jinja2 pour afficher le résultat en HTML
    return render_template('Pages/test/info_server.html', info_server=info_server.items())


@app.route('/')
def index():
    # Exécution du script 'info_server.py' et récupération du dictionnaire de résultat
    result = subprocess.run(['python', './SemaOS/info_server.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    info_server = liste
    
   # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if info_server is None or not isinstance(info_server, dict):
        return "Aucune information sur le serveur disponible"
    
    
    return render_template('Pages/SemaWeb/index.html', info_server=info_server)

@app.route('/tools', methods=['GET', 'POST'])
def tools():
    
    if request.method == 'POST':
        if 'go' in request.form:
            session['speedtest_status'] = 'go'
        elif 'reset' in request.form:
            session['speedtest_status'] = 'reset'
            
        if 'scan' in request.form:
            session['scan_status'] = 'scan'
        elif 'reset' in request.form:
            session['scan_status'] = 'reset'
            
    if request.method == 'GET':
        session['speedtest_status'] = 'reset'
        session['scan_status'] = 'reset'

    # Exécution du script 'materiel_server.py' et récupération du dictionnaire de résultat
    result = subprocess.run(['python', './SemaOS/materiel_server.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    liste = ast.literal_eval(output)
    materiel = liste

    # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if materiel is None or not isinstance(materiel, dict):
        return "Aucune information sur le serveur disponible"

    # Exécution du script 'etat_server' et récupération du dictionnaire de résultat
    result_script = subprocess.run(['python', './SemaOS/etat_server.py'], stdout=subprocess.PIPE)
    output_script = result_script.stdout.decode('utf-8')
    disctionnaire = ast.literal_eval(output_script)
    etat = disctionnaire

    # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if etat is None or not isinstance(etat, dict):
        return "Aucune information sur le serveur disponible"

    # Exécution du script 'info_server.py' et récupération du dictionnaire de résultat
    results = subprocess.run(['python', './SemaOS/info_server.py'], stdout=subprocess.PIPE)
    outputs = results.stdout.decode('utf-8')
    disctionnaires = ast.literal_eval(outputs)
    ip_public = disctionnaires

    # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if ip_public is None or not isinstance(ip_public, dict):
        return "Aucune information sur le serveur disponible"

    if session.get('speedtest_status') == 'go':
        # Exécution du script 'server_speedtest.py' et récupération du dictionnaire de résultat
        resultes = subprocess.run(['python', './SemaOS/server_speedtest.py'], stdout=subprocess.PIPE)
        outputes = resultes.stdout.decode('utf-8')
        disctionnairs = ast.literal_eval(outputes)
        speedtest = disctionnairs

        # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
        if speedtest is None or not isinstance(speedtest, dict):
            return "Aucune information sur le serveur disponible"
    else:
        speedtest = " "

    if session.get('speedtest_status') == 'reset':
        speedtest = " "

    if session.get('scan_status') == 'scan':
        #Exécution du script 'scan.py' et récupération du dictionnaire de résultat
        resultes_scan = subprocess.run(['python', './SemaOS/scan_servers.py'], stdout=subprocess.PIPE)
        outputes_scan = resultes_scan.stdout.decode('utf-8')
        disctionnairees = ast.literal_eval(outputes_scan)
        scan = disctionnairees

        if not isinstance(scan, (dict, list, tuple)):
            raise ValueError("scan_results is not a valid iterable")
        
        # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
        if scan is None or not isinstance(scan, dict):
            return "Aucune information sur le serveur disponible"
        
    
    if session.get('scan_status') == 'reset':
        scan = {}
        

    print(scan)
    print(type(scan))
    return render_template('Pages/SemaWeb/tools.html', materiel=materiel, etat=etat, ip=ip_public, speedtest=speedtest, scan_results=scan.items())

@app.route('/propos')
def about():
    return render_template('Pages/SemaWeb/propos.html')


# Fonction Erreur d'affichage

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 404 (page non trouvée)
@app.errorhandler(404)
def page_not_found(error):
    # Retourne la réponse générée par le template de la page d'erreur HTTP 404, ainsi que le code d'erreur 404
    return render_template('ErrorPages/HTTP404.html'), 404

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 400 (requête incorrecte)
@app.errorhandler(400)
def page_not_found3(error):
    # Retourne la réponse générée par le template de la page d'erreur HTTP 400, ainsi que le code d'erreur 400
    return render_template('ErrorPages/HTTP400.html'), 400

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 500 (erreur interne du serveur)
@app.errorhandler(500)
def page_not_found2(error):
    # Retourne la réponse générée par le template de la page d'erreur HTTP 500, ainsi que le code d'erreur 500
    return render_template('ErrorPages/HTTP500.html'), 500

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 501 (fonctionnalité non implémentée)
@app.errorhandler(501)
def page_not_found4(error):
    # Retourne la réponse générée par le template de la page d'erreur HTTP 501, ainsi que le code d'erreur 501
    return render_template('ErrorPages/HTTP501.html'), 501

@app.errorhandler(404)
def page_not_found(error):
    # Si la ressource n'a pas été modifiée, renvoyer une réponse avec le code d'erreur 304
    return Response(render_template('ErrorPages/HTTP304.html'), status=304)

@app.route('/<path:path>')
def catch_all(path):
    # Si l'utilisateur accède à un dossier qui n'existe pas, générer une erreur 404
    abort(404)

if __name__ == '__main__':
    # on lance l'application Flask avec le mode debug activé et sur l'adresse IP de la machine ainsi que sur le port donnée
    app.run(host=ip(),port=80,debug=False)

