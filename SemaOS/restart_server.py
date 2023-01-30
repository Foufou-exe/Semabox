#!/usr/bin/env python3.11.1

# Description: Ce fichier contient les fonctions permettant de redémarrer ou d'éteindre le serveur.

# Importation des modules Python nécessaires
import subprocess
import platform

# Définition des fonctions
def redemarrer()->dict:
    """
        Description:
            Cette fonction redémarre le serveur.
        
        Returns:
            str: Un message indiquant que le redémarrage du serveur est en cours.
    """

    if platform.system() == "Windows":
        print({"message": "ok"})
        subprocess.call(["shutdown", "/r"])
    else:
        print({"message": "ok"})
        subprocess.call(["reboot"])
    
if __name__ == "__main__":
    redemarrer()