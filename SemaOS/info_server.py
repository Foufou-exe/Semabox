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
import requests
import ipaddress
import os



# Importe de nos modules Python personnalisés
from SemaOS.generation_UID import lire_fichier



def get_hostname()->str:
    
    """
        Cette fonction retourne le nom d'hôte de la machine sur laquelle le code est exécuté.
    """
    
    return platform.node()


# def get_interface_openvpn()->str:
        
#     """
#         Cette fonction retourne le nom de l'interface réseau utilisée par OpenVPN.
#     """
#     for process in psutil.process_iter():
#         if process.name() == "openvpn":
#             for conn in process.connections():
#                 if conn.type == socket.SOCK_STREAM:
#                     openvpn = conn.raddr.interface
                    
#     if openvpn:
#         addresses = netifaces.ifaddresses(openvpn)
#     if netifaces.AF_INET in addresses:
#         for link in addresses[netifaces.AF_INET]:
#             return link['addr']
        
    


def get_ip_address() -> str:

    """
        Cette fonction retourne l'adresse IP de la machine sur laquelle le code est exécuté.
    """

    return socket.gethostbyname(socket.gethostname())




def get_address_network(ip=get_ip_address()) -> str:

    """
        Description:
            Cette fonction récupère l'adresse de réseau à partir d'une adresse IP et d'un masque de sous-réseau
            
        Args:
            ip (str) : adresse IP
            
        Returns:
            str : adresse de réseau
    """

    # Création d'un objet qui contient l'adresse IP et le masque de sous-réseau
    ip_obj = ipaddress.IPv4Interface(ip+"/24")

    # Récupération de l'adresse de réseau
    network = ip_obj.network # l'adresse réseau
    return network





def get_dns(ip)->str:   
     
    """
        Cette fonction retourne le nom de domaine associé à l'adresse IP spécifiée.
        
        Paramètres :
            - ip (str) : adresse IP pour laquelle on souhaite récupérer le nom de domaine.
    """
    
    dns_resulte = socket.gethostbyaddr(ip)
    return dns_resulte[0] + "".join(".cma4.box")





def get_version_semabox()->str:
    
    """
        Cette fonction retourne la version de SemaBox en lisant le fichier "version.txt" dans le répertoire "Application/modules".
    """
    if os.name == 'nt': # Windows
        file_path = os.path.join("SemaOS", "version.txt")
    else: # Linux ou autre
        file_path = os.path.join("/Semabox/SemaOS", "version.txt")

    with open(file_path, "r") as f:
        return f.readline()
    
    
    
    
def get_public_ip()->str:
    response = requests.get("http://ipinfo.io/json")
    data = response.json()
    return data["ip"]

def api_get_public_ip(ip=get_public_ip())->dict:
    return {"ip_public": ip}




def api_info_server(version=get_version_semabox(),lire_uid=lire_fichier(),hostname=get_hostname(),ip=get_ip_address(),dns=get_dns(get_ip_address()),ip_public=get_public_ip())->dict:
    
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
    
    
    
    
def cli_get_info_server(version=get_version_semabox(),lire_uid=lire_fichier(),hostname=get_hostname(),ip=get_ip_address(),dns=get_dns(get_ip_address()),ip_public=get_public_ip()):
    
    """
        Description:
            Cette fonction retourne un dictionnaire contenant les informations du serveur
            
        Returns:
            dict: informations du serveur
    """
    return {
        'hostname': hostname,
        'ip': ip,
        'ip_public': ip_public,
        'dns': dns,
        'uid': lire_uid,
        'version_semabox': version
    }
    
    
    
    
# Si ce fichier est exécuté directement, on appelle la fonction api_info_server()
if __name__ == "__main__":
    api_info_server()

