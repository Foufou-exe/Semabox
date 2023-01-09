# Description: Ce fichier contient les fonctions permettant de redémarrer ou d'éteindre le serveur.

# Importation des modules Python nécessaires
import subprocess

# Définition des fonctions
def redemarrer():
    """
        Description:
            Cette fonction redémarre le serveur.
        
        Returns:
            str: Un message indiquant que le redémarrage du serveur est en cours.
    """
    subprocess.run(["reboot"])
    resultat = {"resultat": "Redémarrage du serveur en cours"}
    print(resultat)

    
if __name__ == "__main__":
    redemarrer()