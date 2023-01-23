#!/usr/bin/env python3.11.1

import subprocess
import platform 

def pre_installation():
  """
    Description:
        Cette fonction exécute le script de génération d'un identifiant unique (UID) pour l'installation de SemaOS.
  """
  if platform.system() == "Windows":
    subprocess.run(["python", "./SemaOS/generation_UID.py"])
  elif platform.system() == "Linux":
    subprocess.run(["sudo","python", "/Semabox/SemaOS/generation_UID.py"])


if __name__ == "__main__":
  pre_installation()