#!/usr/bin/env python3.11.1

# Description: Ce fichier contient les fonctions permettant de redémarrer ou d'éteindre le serveur.

# Importation des modules Python nécessaires
import subprocess  # Pour les commandes shell
import os  # Pour les commandes shell

# Définition des fonctions
def redemarrer() -> dict:
    """
    Description:
        Cette fonction redémarre le serveur.

    Returns:
        str: Un message indiquant que le redémarrage du serveur est en cours.
    """
    # Redémarre le serveur
    if os.name == "nt":
        print({"message": "ok"})  # Affiche un message de confirmation
        subprocess.call(["shutdown", "/r"])  # Redémarre le serveur
    else:
        print({"message": "ok"})  # Affiche un message de confirmation
        subprocess.call(["reboot"])  # Redémarre le serveur


if __name__ == "__main__":
    redemarrer()
