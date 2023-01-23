#!/usr/bin/env python3.11.1

import sys
import subprocess

# Ajout du chemin vers le dossier Application pour qu'on puisse importer nos modules
sys.path.append("..") # On retourne dans le dossier Principal Semabox
sys.path.append("SemaOS") # On ajoute le chemin './SemaOS' au path de sys pour pouvoir importer les modules de ce répertoire
# Importe de nos modules Python personnalisés
from info_server import get_ip_address as ip, get_hostname as hostname, get_dns as dns_semabox, get_version_semabox as version_semabox, get_public_ip as ip_public
from generation_UID import lire_fichier as uid

def pre_installation():
  """
    Description:
        Cette fonction exécute le script de génération d'un identifiant unique (UID) pour l'installation de SemaOS.
  """
  subprocess.run(["python", "./SemaOS/generation_UID.py"])


if __name__ == "__main__":
    pre_installation()
