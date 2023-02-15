#!/usr/bin/env python3.11.1

# Importe le module os
import subprocess  # Importe le module subprocess pour lancer des commandes shell
import sys # Importe le module sys pour ajouter le chemin d'accès au module info_server.py

# Ajoute le chemin d'accès au module info_server.py
sys.path.append("SemaOS")
# Importe la fonction get_ip_address() du module info_server
from info_server import get_ip_address

# Définit une fonction qui prend en paramètre l'adresse IP du serveur à vérifier
def server_is_up(host=get_ip_address()):
    """
        Description:
            Cette fonction vérifie si le serveur est en ligne en envoyant une requête ping à l'adresse IP spécifiée.

        Args:
            host (str): L'adresse IP du serveur à vérifier.

        Returns:
            bool: True si le serveur est en ligne, False sinon.
    """

    try:
        subprocess.check_output(f'ping -n 1 {host}', shell=True, universal_newlines=True) # Envoie une requête ping au serveur
        resultat1 = {"etat_semabox": "up"} # Si le serveur répond, retourne True
        print(resultat1) # Affiche le résultat
    except subprocess.CalledProcessError as e: # Si le serveur ne répond pas, retourne False
        resultat2 = {"etat_semabox": "down"} # Si le serveur répond, retourne True
        print(resultat2) # Affiche le résultat

def api_server_is_up(host=get_ip_address()):
    """
        Description:
            Cette fonction vérifie si le serveur est en ligne en envoyant une requête ping à l'adresse IP spécifiée.

        Args:
            host (str): L'adresse IP du serveur à vérifier.

        Returns:
            bool: True si le serveur est en ligne, False sinon.
    """

    try:
        subprocess.check_output(f'ping -n 1 {host}', shell=True, universal_newlines=True) # Envoie une requête ping au serveur
        resultat1 = {"etat_semabox": "up"} # Si le serveur répond, retourne True
        return resultat1 # Affiche le résultat
    except subprocess.CalledProcessError as e: # Si le serveur ne répond pas, retourne False
        resultat2 = {"etat_semabox": "down"} # Si le serveur répond, retourne True
        return resultat2 # Affiche le résultat
        
        
# Si le module est exécuté directement (et non importé)
if __name__ == "__main__":
    server_is_up()

