
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

