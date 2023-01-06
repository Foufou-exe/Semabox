# Importation des modules Pythons nécessaires
import sys
import os

# Ajout du chemin vers le dossier Application pour qu'on puisse importer nos modules
sys.path.append("Application")

# Importe de nos modules Python personnalisés
from modules.info_server import get_dns, get_hostname, get_ip_address
from modules.generation_UID import *


def premier_lancement():
    if not os.path.exists("SEMABOX_UID"):
        creation_dossier(generate_id())
    return lire_fichier()



if __name__ == "__main__":
    