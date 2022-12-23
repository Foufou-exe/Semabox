import socket
import sys
import os
sys.path.append("Application")
from modules.info_server import *
from modules.generation_UID import *

def premier_lancement():
    if not os.path.exists("SEMABOX_UID"):
        creation_dossier(generate_id())
    
    retour_uid = lire_fichier()
    return retour_uid
    


def ecriture_fichier(uid):
    global name_file
    hostname = get_hostname()
    ip = get_ip_address()
    dns = get_dns(ip)
    
    liste_info = [dns,hostname,ip,uid]
    name_file = dns + ".csv"
    os.chdir("Application/install")
    if not os.path.exists(name_file):
        with open(name_file, 'w', encoding='utf-8') as my_file:
            my_file.write(','.join(liste_info))
    else:
        print("Le fichier existe déjà")


def envoie_information():    
    # Création du client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connexion au serveur
    client.connect(('localhost', 19999))
    
    # Envoi de la requête au serveur
    client.send(name_file.encode(encoding='utf-8', errors='strict'))

    # Réception des résultats du serveur
    results = client.recv(1024)
    print(results)

    # Fermeture de la connexion
    client.close()


if __name__ == "__main__":
   ecriture_fichier(premier_lancement())
