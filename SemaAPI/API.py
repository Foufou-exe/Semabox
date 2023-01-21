
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


# from latence import get_latency

# Création de l'application Flask
app = Flask(__name__, template_folder='template')
app.secret_key = "./SemaAPI/secret_key"

# Définition d'une route qui accepte les méthodes POST
@app.route('/api/<script>', methods=['POST'])
def create_script(script):
    """
        Description de la fonction create_script:
            Cette fonction crée un script en l'exécutant à l'aide de subprocess.run,
            puis récupère la sortie standard du script exécuté, la convertit en un dictionnaire Python,
            vérifie si le dictionnaire est valide et non vide,
            puis convertit le dictionnaire en une chaîne de caractères au format JSON
            et la renvoie avec l'en-tête 'Content-Type: application/json'
    """
    
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
    """
        Description de la fonction get_script: 
            Cette fonction récupère un script en l'exécutant à l'aide de subprocess.run,
            puis récupère la sortie standard du script exécuté, la convertit en un dictionnaire Python,
            vérifie si le dictionnaire est valide et non vide,
            puis convertit le dictionnaire en une chaîne de caractères au format JSON
            et la renvoie avec l'en-tête 'Content-Type: application/json'
    """
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

@app.route('/')
def index():
    """
        Description de la fonction index:
            Cette fonction affiche les informations relatives au serveur en exécutant le script 'info_server.py' et en récupérant le dictionnaire de résultat.
            Si le dictionnaire est vide, une erreur HTTP 404 est retournée avec un message d'erreur personnalisé "Aucune information sur le serveur disponible"
            La page html 'index.html' est ensuite rendue en utilisant les informations récupérées.
    """
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
    """
        Cette fonction gère la page des outils en effectuant les étapes suivantes:

        - Elle vérifie la méthode HTTP utilisée (GET ou POST)
        - Si la méthode est POST, elle vérifie si les boutons 'go' ou 'reset' pour le test de vitesse, ou 'scan' ou 'reset' pour le scan réseau ont été soumis, et enregistre le statut correspondant dans les sessions.
        - Si la méthode est GET, elle réinitialise les statuts des sessions pour le test de vitesse et le scan réseau.
        - Elle exécute le script 'materiel_server.py' et récupère le résultat sous forme de dictionnaire, vérifie si le dictionnaire est valide et non vide, sinon renvoie un message d'erreur "Aucune information sur le serveur disponible".
        - Elle exécute le script 'etat_server.py' et récupère le résultat sous forme de dictionnaire, vérifie si le dictionnaire est valide et non vide, sinon renvoie un message d'erreur "Aucune information sur le serveur disponible".
        - Elle exécute le script 'info_server.py' et récupère le résultat sous forme de dictionnaire, vérifie si le dictionnaire est valide et non vide, sinon renvoie un message d'erreur "Aucune information sur le serveur disponible".
        - Si le statut de la session pour le test de vitesse est 'go', elle exécute le script 'server_speedtest.py' et récupère le résultat sous forme de dictionnaire, vérifie si le dictionnaire est valide et non vide, sinon renvoie un message d'erreur "Aucune information sur le serveur disponible".
        - Si le statut de la session pour le scan réseau est 'scan', elle exécute le script 'scan_servers.py' et récupère le résultat sous forme de dictionnaire, vérifie si le dictionnaire est valide et non vide, sinon renvoie un message d'erreur "Aucune information sur le serveur disponible".
        Enfin, elle utilise les informations récupérées pour rendre les templates correspondants.
            - En somme, cette fonction gère l'affichage des informations relatives à l'état du matériel, de l'état du serveur, de l'IP public, des résultats des tests de vitesse et des scans réseau sur la page des outils en se basant sur les actions de l'utilisateur et en vérifiant la validité des informations récupérées.
            
    """
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
        
    return render_template('Pages/SemaWeb/tools.html', materiel=materiel, etat=etat, ip=ip_public, speedtest=speedtest, scan_results=scan.items())

@app.route('/propos')
def about():
    """ 
        Description:
            Cette fonction est un gestionnaire de route pour la page 'A propos'. Elle est appelée chaque fois qu'une demande est effectuée sur la page 'A propos'.
    """
    return render_template('Pages/SemaWeb/propos.html')


# Fonction Erreur d'affichage

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 404 (page non trouvée)
@app.errorhandler(404)
def page_not_found(error):
    """
        Description:
            Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 404. Elle est appelée chaque fois qu'une demande entraîne une erreur 404. 
            Elle renvoie la réponse générée par le modèle de la page d'erreur HTTP 404, ainsi que le code d'erreur 404.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 404, ainsi que le code d'erreur 404
    return render_template('ErrorPages/HTTP404.html'), 404

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 400 (requête incorrecte)
@app.errorhandler(400)
def page_not_found3(error):
    """ 
        Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 400 (requête incorrecte). Elle est appelée chaque fois qu'une demande entraîne une erreur 400.
        Elle renvoie la réponse générée par le modèle de la page d'erreur HTTP 400, ainsi que le code d'erreur 400.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 400, ainsi que le code d'erreur 400
    return render_template('ErrorPages/HTTP400.html'), 400

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 500 (erreur interne du serveur)
@app.errorhandler(500)
def page_not_found2(error):
    """ 
        Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 500 (erreur interne du serveur). Elle est appelée chaque fois qu'une demande entraîne une erreur 500. 
        Elle renvoie la réponse générée par le modèle de la page d'erreur HTTP 500, ainsi que le code d'erreur 500.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 500, ainsi que le code d'erreur 500
    return render_template('ErrorPages/HTTP500.html'), 500

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 501 (fonctionnalité non implémentée)
@app.errorhandler(501)
def page_not_found4(error):
    """ 
        Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 501 (fonctionnalité non implémentée). Elle est appelée chaque fois qu'une demande entraîne une erreur 501.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 501, ainsi que le code d'erreur 501
    return render_template('ErrorPages/HTTP501.html'), 501

@app.errorhandler(404)
def page_not_found(error):
    """ 
        Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 404 (page non trouvée). Elle est appelée chaque fois qu'une demande entraîne une erreur 404.
    """
    # Si la ressource n'a pas été modifiée, renvoyer une réponse avec le code d'erreur 304
    return Response(render_template('ErrorPages/HTTP304.html'), status=304)

@app.route('/<path:path>')
def catch_all(path):
    """ 
        Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 404 (page non trouvée). Elle est appelée chaque fois qu'une demande entraîne une erreur 404.
    """
    # Si l'utilisateur accède à un dossier qui n'existe pas, générer une erreur 404
    abort(404)

if __name__ == '__main__':
    # on lance l'application Flask avec le mode debug activé et sur l'adresse IP de la machine ainsi que sur le port donnée
    app.run(host="0.0.0.0",port=80,debug=False)

