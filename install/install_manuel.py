#!/usr/bin/env python3.11.1

import subprocess
import os

def pre_installation():
  """
    Description:
        Cette fonction exécute le script de génération d'un identifiant unique (UID) pour l'installation de SemaOS.
  """
  file_path = os.path.join("SemaOS","generation_UID.py")
  subprocess.run(["python", file_path])



if __name__ == "__main__":
  pre_installation()