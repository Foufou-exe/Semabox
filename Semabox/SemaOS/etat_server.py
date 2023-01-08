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
    return "Redémarrage du serveur en cours"
    
def eteindre():
    """
    Description:
        Cette fonction éteint le serveur.
    
    Returns:
        str: Un message indiquant que l'arrêt du serveur est en cours.
    """
    subprocess.run(["shutdown", "-h", "now"])
    return "Arrêt du serveur en cours"


    
if __name__ == "__main__":
    redemarrer()