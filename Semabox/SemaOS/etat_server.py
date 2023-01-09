# Importe le module os
import os

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
    # Envoie une requête ping au serveur en utilisant la commande 'ping' du système et stocke le résultat dans la variable 'response'
    response = os.system(f"ping {host}")
    
    # Retourne True si la commande 'ping' a réussi (c'est-à-dire si le serveur est en ligne), False sinon
    return response == 0

# Si le module est exécuté directement (et non importé)
if __name__ == "__main__":
    # Si le serveur est en ligne
    if server_is_up(get_ip_address()):
        # Crée un dictionnaire contenant l'état 'up' du serveur et l'affiche à l'écran
        resultat1 = {"etat": "up"}
        print(resultat1)
    # Si le serveur n'est pas en ligne
    else:
        # Crée un dictionnaire contenant l'état 'down' du serveur et l'affiche à l'écran
        resultat2 = {"etat": "down"}
        print(resultat2)
