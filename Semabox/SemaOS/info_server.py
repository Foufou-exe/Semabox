# Import des modules Python nécessaires
import socket
import platform
import sys
import requests


# Ajout du chemin vers le dossier Application pour qu'on puisse importer nos modules
sys.path.append('Semabox/SemaOS')

# Importe de nos modules Python personnalisés
from generation_UID import lire_fichier



def get_hostname():
    
    """
        Cette fonction retourne le nom d'hôte de la machine sur laquelle le code est exécuté.
    """
    
    return platform.node()

def get_ip_address():
    
    """
        Cette fonction retourne l'adresse IP de la machine sur laquelle le code est exécuté.
    """
    
    return socket.gethostbyname(socket.gethostname())


def get_dns(ip):   
     
    """
        Cette fonction retourne le nom de domaine associé à l'adresse IP spécifiée.
        
        Paramètres :
            - ip (str) : adresse IP pour laquelle on souhaite récupérer le nom de domaine.
    """
    
    dns_resulte = socket.gethostbyaddr(ip)
    return dns_resulte[0] + "".join(".cma4.box")

def get_version_semabox():
    
    """
        Cette fonction retourne la version de SemaBox en lisant le fichier "version.txt" dans le répertoire "Application/modules".
    """
    
    with open("Semabox/SemaOS/version.txt", "r") as f:
        return f.readline()
    
def get_public_ip():
    url = "https://api.ipify.org"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Unable to fetch public IP."

def api_info_server():
    
    """
        Cette fonction retourne un dictionnaire contenant des informations sur le serveur sur lequel le code est exécuté.
    """
    version = get_version_semabox()
    lire_uid = lire_fichier()
    hostname = get_hostname()
    ip = get_ip_address()
    dns = get_dns(ip)
    ip_public = get_public_ip()
    info_server = {
        'hostname': hostname,
        'ip': ip,
        'ip_public': ip_public,
        'dns': dns,
        'uid': lire_uid,
        'version_semabox': version
    }
    print(info_server)
    

# Si ce fichier est exécuté directement, on appelle la fonction api_info_server()
if __name__ == "__main__":
    api_info_server()
