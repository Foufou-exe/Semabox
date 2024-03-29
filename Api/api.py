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
import subprocess  # Module qui permet d'exécuter des commandes système
import ast  # Module qui permet de convertir une chaîne de caractères en dictionnaire Python
import json  # Module qui permet de convertir un dictionnaire Python en une chaîne de caractères JSON
import sys
import os
import logging  # Module qui permet de gérer les logs
import time  # Module qui permet de gérer le temps
import asyncio  # Module qui permet de gérer les boucles d'événements

from version import semaweb_version  # Import de la version de l'application

# Ajout du chemin d'accès au dossier parent
sys.path.append(
    os.path.join(os.path.dirname(__file__), "..")
)  # Ajout du chemin d'accès au dossier parent ( permet de retourné au dossier parent)

# Import des modules Python personnalisés
from Modules import InfoServer, get_info_system  # Import du module InfoServer
from Modules import ScanPort  # Import des modules ScanPort et ScanPortOtherServers
from Modules import Speedtest  # Import du module Speedtest
from Modules import api_scan_port_other_machine

"""
    Description de la Librairie Flask:
        Les modules Flask :
            Flask = Framework Python pour créer des applications Web  
            request = module qui permet de récupérer les données envoyées dans une requête HTTP
            jsonify = module qui permet de convertir un dictionnaire Python en une chaîne de caractères JSON
            abort = module qui permet de retourner une erreur HTTP
"""

# Import des modules Flask
from flask import Flask, render_template, jsonify, abort, Response, request, session
from flask_caching import Cache  # Import du module Flask-Cache


# Création de l'application Flask
app = Flask(__name__)
app.secret_key = "keys/secret_key"  # Clé secrète pour la session
cache = Cache(
    app, config={"CACHE_TYPE": "SimpleCache", "CACHE_DEFAULT_TIMEOUT": 30}
)  # Configuration du cache


# Variable qui contient le nom du fichier de logs
name_file = f'Flask_{time.strftime("%Y_%m_%d_%H")}.log'  # Nom du fichier de logs

if sys.platform == "win32":  # Windows
    direction_file = f"Api/logs/{name_file}"
else:
    direction_file = f"../Api/logs/{name_file}"
    if not os.path.exists(direction_file):
        open(direction_file, "w")

# Import du logging pour les logs
logging.basicConfig(
    filename=direction_file,
    format="%(asctime)s--[%(levelname)s] = %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
)


# Définition de la fonction after_request qui s'exécute après chaque requête HTTP
@app.after_request
def after_request(response):
    """
    C'est une fonction Flask en Python avec le décorateur @app.after_request qui s'exécute après chaque requête HTTP.
    Il enregistre une chaîne contenant la méthode HTTP, l'URL et le code de statut de la réponse en utilisant la méthode info du journal associé à l'application Flask.
    Finalement, il retourne la réponse HTTP.
    """
    log_string = f"{request.method} {request.url} {response.status_code}"
    app.logger.info(log_string)
    return response


# Définition d'une route qui accepte les méthodes POST , GET
@app.route("/api/<script>", methods=["POST", "GET"])
def create_script(script) -> dict:
    """
    Description de la fonction create_script:
        Cette fonction exécute le script spécifié en utilisant subprocess.run et retourne une représentation en chaîne de caractères JSON de la sortie du script.
    """

    # Définir le chemin d'accès au fichier en fonction du système d'exploitation
    if os.name == "nt":  # Windows
        if script == "info.py":
            file_path = os.path.join("Modules/Information", script)
        elif script == "materiel.py":
            file_path = os.path.join("Modules/Information", script)
        elif script == "scanAllServer.py":
            file_path = os.path.join("Modules/Scan", script)
        elif script == "scanPort.py":
            file_path = os.path.join("Modules/Scan", script)
        elif script == "speedtest.py":
            file_path = os.path.join("Modules/Speedtest", script)
        elif script == "restart.py":
            file_path = os.path.join("Modules/Serveur", script)
        elif script == "update.py":
            file_path = os.path.join("Modules/Serveur", script)
    else:  # Linux ou autre
        if script == "info.py":
            file_path = os.path.join("../Semabox/Modules/Information", script)
        elif script == "materiel.py":
            file_path = os.path.join("../Semabox/Modules/Information", script)
        elif script == "scanAllServer.py":
            file_path = os.path.join("../Semabox/Modules/Scan", script)
        elif script == "scanPort.py":
            file_path = os.path.join("../Semabox/Modules/Scan", script)
        elif script == "speedtest.py":
            file_path = os.path.join("../Semabox/Modules/Speedtest", script)
        elif script == "restart.py":
            file_path = os.path.join("../Semabox/Modules/Serveur", script)
        elif script == "update.py":
            file_path = os.path.join("../Semabox/Modules/Serveur", script)

    # Exécution du script en utilisant subprocess.run
    result = subprocess.run(["python", file_path], stdout=subprocess.PIPE)

    # Récupération de la sortie standard du script exécuté
    output = result.stdout.decode("utf-8")

    # Conversion de la sortie du script en un dictionnaire Python
    result_script = ast.literal_eval(output)

    # Si la liste est vide ou que ce n'est pas un dictionnaire, on retourne un message d'erreur
    if result_script is None or not isinstance(result_script, dict):
        return "Aucune information sur le serveur disponible"

    # Retour de la chaîne de caractères au format JSON avec l'en-tête 'Content-Type: application/json'
    return jsonify(result_script_json=result_script)


# Définition d'une route qui accepte les méthodes POST, GET
@app.route("/api/scanPortOtherServer/<ip>", methods=["POST", "GET"])
def add_script(ip):
    """
    Description de la fonction create_script:
        Cette fonction exécute le script spécifié en utilisant subprocess.run et retourne une représentation en chaîne de caractères JSON de la sortie du script.
    """

    result_script = api_scan_port_other_machine(str(ip))

    # Si la liste est vide ou que ce n'est pas un dictionnaire, on retourne un message d'erreur
    if result_script is None or not isinstance(result_script, dict):
        return "Aucune information sur le serveur disponible"

    # Retour de la chaîne de caractères au format JSON avec l'en-tête 'Content-Type: application/json'
    return jsonify(result_script_json=result_script)


@app.route("/")  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def index():
    """
    Description de la fonction index:
        Cette fonction affiche les informations relatives au serveur en exécutant le script 'info_server.py' et en récupérant le dictionnaire de résultat.
        Si le dictionnaire est vide, une erreur HTTP 404 est retournée avec un message d'erreur personnalisé "Aucune information sur le serveur disponible"
        La page html 'index.html' est ensuite rendue en utilisant les informations récupérées.
    """

    info_server = InfoServer.api_info_server()
    version_web = semaweb_version

    # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if info_server is None or not isinstance(info_server, dict):
        return "Aucune information sur le serveur disponible"

    return render_template("index.html", info_server=info_server, version=version_web)


@app.route(
    "/tools", methods=["GET", "POST"]
)  # Définition d'une route qui accepte les méthodes POST, GET
def tools():
    """
    La fonction tools implémente le point d'entrée '/tools' d'une application Flask et gère les requêtes GET et POST.

    Pour les requêtes POST, elle met à jour les statuts speedtest_status et scan_status en fonction de la présence de 'go' ou 'reset' dans la requête.

    Pour les requêtes GET, elle met à jour les statuts speedtest_status et scan_status en 'reset'.

    Elle utilise les fonctions api_get_info_system, api_server_is_up, api_get_public_ip, api_web_speedtest et api_web_scan_nmap pour récupérer diverses informations sur le serveur. Si les informations récupérées ne sont pas valides (vides ou pas des objets dict), elle renvoie une erreur HTTP 404 avec un message d'erreur personnalisé.

    Enfin, elle retourne une vue en utilisant le template 'Pages/SemaWeb/tools.html' avec les informations récupérées sur le serveur.
    """
    if request.method == "POST":
        if "go" in request.form:
            session["speedtest_status"] = "go"
        elif "reset" in request.form:
            session["speedtest_status"] = "reset"

        if "scan" in request.form:
            session["scan_status"] = "scan"
        elif "reset" in request.form:
            session["scan_status"] = "reset"

    if request.method == "GET":
        session["speedtest_status"] = "reset"
        session["scan_status"] = "reset"

    # Appel de la fonction api_get_info_system() pour récupérer les informations relatives au serveur
    materiel = get_info_system()

    # Appel de la fonction api_get_public_ip() pour récupérer les informations relatives à l'IP public
    ip_public = InfoServer.api_get_public_ip()

    # # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
    if ip_public is None or not isinstance(ip_public, dict):
        return "Aucune information sur le serveur disponible"

    if materiel is None or not isinstance(materiel, dict):
        return "Aucune information sur le serveur disponible"

    if session.get("speedtest_status") == "go":
        # Appel de la fonction api_web_speedtest() pour récupérer les informations relatives au test de vitesse
        speedtest = asyncio.run(Speedtest.api_web_speedtest())

        # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
        if speedtest is None or not isinstance(speedtest, dict):
            return "Aucune information sur le serveur disponible"
    else:
        speedtest = " "

    if session.get("speedtest_status") == "reset":
        speedtest = " "

    if session.get("scan_status") == "scan":
        # Appel de la fonction api_web_scan_nmap() pour récupérer les informations relatives au scan réseau
        scan = ScanPort.api_scan()

        if not isinstance(scan, (dict, list, tuple)):
            raise ValueError("scan_results is not a valid iterable")

        # Si le dictionnaire est vide, on retourne une erreur HTTP 404 avec un message d'erreur personnalisé
        if scan is None or not isinstance(scan, dict):
            return "Aucune information sur le serveur disponible"

    if session.get("scan_status") == "reset":
        scan = {}

    version_web = semaweb_version

    return render_template(
        "tools.html",
        materiel=materiel,
        version=version_web,
        ip=ip_public,
        speedtest=speedtest,
        scan_results=scan.items(),
    )


@app.route("/propos")  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def about():
    """
    Description:
        Cette fonction est un gestionnaire de route pour la page 'A propos'. Elle est appelée chaque fois qu'une demande est effectuée sur la page 'A propos'.
    """
    version_web = semaweb_version

    return render_template("propos.html", version=version_web)


# Fonction Erreur d'affichage

# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 404 (page non trouvée)
@app.errorhandler(404)  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def page_not_found(error):
    """
    Description:
        Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 404. Elle est appelée chaque fois qu'une demande entraîne une erreur 404.
        Elle renvoie la réponse générée par le modèle de la page d'erreur HTTP 404, ainsi que le code d'erreur 404.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 404, ainsi que le code d'erreur 404
    return render_template("ErrorPages/HTTP404.html"), 404


# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 400 (requête incorrecte)
@app.errorhandler(400)  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def page_not_found3(error):
    """
    Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 400 (requête incorrecte). Elle est appelée chaque fois qu'une demande entraîne une erreur 400.
    Elle renvoie la réponse générée par le modèle de la page d'erreur HTTP 400, ainsi que le code d'erreur 400.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 400, ainsi que le code d'erreur 400
    return render_template("ErrorPages/HTTP400.html"), 400


# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 500 (erreur interne du serveur)
@app.errorhandler(500)  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def page_not_found2(error):
    """
    Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 500 (erreur interne du serveur). Elle est appelée chaque fois qu'une demande entraîne une erreur 500.
    Elle renvoie la réponse générée par le modèle de la page d'erreur HTTP 500, ainsi que le code d'erreur 500.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 500, ainsi que le code d'erreur 500
    return render_template("ErrorPages/HTTP500.html"), 500


# Définit un gestionnaire d'erreur pour le code d'erreur HTTP 501 (fonctionnalité non implémentée)
@app.errorhandler(501)  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def page_not_found4(error):
    """
    Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 501 (fonctionnalité non implémentée). Elle est appelée chaque fois qu'une demande entraîne une erreur 501.
    """
    # Retourne la réponse générée par le template de la page d'erreur HTTP 501, ainsi que le code d'erreur 501
    return render_template("ErrorPages/HTTP501.html"), 501


@app.errorhandler(404)  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def page_not_found(error):
    """
    Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 404 (page non trouvée). Elle est appelée chaque fois qu'une demande entraîne une erreur 404.
    """
    # Si la ressource n'a pas été modifiée, renvoyer une réponse avec le code d'erreur 304
    return Response(render_template("ErrorPages/HTTP304.html"), status=304)


@app.route("/<path:path>")  # Définition d'une route qui accepte les méthodes GET
@cache.cached()  # Cache la page html
def catch_all(path):
    """
    Cette fonction est un gestionnaire d'erreur pour l'erreur HTTP 404 (page non trouvée). Elle est appelée chaque fois qu'une demande entraîne une erreur 404.
    """
    # Si l'utilisateur accède à un dossier qui n'existe pas, générer une erreur 404
    abort(404)


if __name__ == "__main__":
    # on lance l'application Flask avec le mode debug activé et sur l'adresse IP de la machine ainsi que sur le port donnée
    app.run(host="0.0.0.0", port=80, debug=False)
