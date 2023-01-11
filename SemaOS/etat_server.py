#!/usr/bin/env python3.11.1

# Importe le module os
import subprocess

# Importe la fonction get_ip_address() du module info_server
from info_server import get_ip_address

# Définit une fonction qui prend en paramètre l'adresse IP du serveur à vérifier
def server_is_up(host):
    """
        Description:
            Cette fonction vérifie si le serveur est en ligne en envoyant une requête ping à l'adresse IP spécifiée.

        Args:
            host (str): L'adresse IP du serveur à vérifier.

        Returns:
            bool: True si le serveur est en ligne, False sinon.
    """

    try:
        response = subprocess.check_output(
            f'ping -n 1 {host}', shell=True, universal_newlines=True
        )
        resultat1 = {"etat_semabox": "up"}
        print(resultat1)
    except subprocess.CalledProcessError as e:
        resultat2 = {"etat_semabox": "down"}
        print(resultat2)
        
        
# Si le module est exécuté directement (et non importé)
if __name__ == "__main__":
    server_is_up(host=get_ip_address())

