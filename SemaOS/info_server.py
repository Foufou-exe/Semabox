#!/usr/bin/env python3.11.1
# Description: Ce fichier contient des fonctions permettant de récupérer des informations sur le serveur sur lequel le code est exécuté.

"""
    Description:
        Ce module contient des fonctions permettant de récupérer des informations sur le serveur sur lequel le code est exécuté. 
        Les informations incluent le nom d'hôte, l'adresse IP, l'adresse IP publique, le nom de domaine, l'uid généré par generation_UID.py et la version de Semabox. 
        Il contient également des fonctions pour redémarrer ou éteindre le serveur, et pour vérifier si le serveur est en ligne.
"""


# Import des modules Python nécessaires
import socket
import platform
import sys
import requests


# Ajout du chemin vers le dossier Application pour qu'on puisse importer nos modules
# sys.path.append('')

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
    
    with open("./SemaOS/version.txt", "r") as f:
        return f.readline()
    
def get_public_ip():
    url = "https://api.ipify.org"
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return "Unable to fetch public IP."

def api_info_server(version,lire_uid,hostname,ip,dns,ip_public)->dict:
    
    """
        Description:
            Cette fonction retourne un dictionnaire contenant des informations sur le serveur sur lequel le code est exécuté, telles que le nom d'hôte, l'adresse IP, l'adresse IP publique, le nom de domaine, l'uid généré par generation_UID.py et la version de Semabox.
    """
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
    api_info_server(
        version=get_version_semabox(),
        lire_uid=lire_fichier(),
        hostname=get_hostname(),
        ip=get_ip_address(),
        dns=get_dns(get_ip_address()),
        ip_public=get_public_ip()
    )
