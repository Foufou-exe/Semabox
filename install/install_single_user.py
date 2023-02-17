#!/usr/bin/env python3.11.1

# Ajout de modules Python
import contextlib
import sys
import subprocess
import os

# Ajout de modules personnalisés
from install_enterprise import pre_installation

def version_python()->None:
    """
        Description: Cette fonction permet de vérifier la version de Python utilisée.
            - Si la version de Python est 3.11.1, le script continue son exécution.
        Sinon
            - Si la version de Python est différente de 3.11.1 alors on installe la version 3.11.1 (Linux) ou on demande à l'utilisateur d'installer la version 3.11.1 (Windows
        Paramètres: Aucun
        Retour: Aucun
        
    """
    
    if sys.version_info.major == 3 and sys.version_info.minor == 11 and sys.version_info.micro == 1:
        pass
    else:
        if sys.platform == "linux":
            subprocess.run(["bash", "python3_11_1", "install_python3.11.1.sh"])
        else:
            subprocess.run(["python3_11_1", "install_python3.11.1.ps1"])

            

def define_permissions_linux() -> None:
    """
        Description: Cette fonction permet de définir les permissions d'exécution du script.
            - Si le script est exécuté sur Linux, on vérifie si l'utilisateur a les permissions d'exécution.
            - Si l'utilisateur a les permissions d'exécution, le script continue son exécution(Windows)
        Paramètres: Aucun
        Retour: Pour Linux
            - Si l'utilisateur n'a pas les permissions d'exécution, on demande à l'utilisateur de saisir son mot de passe pour lui accorder les permissions d'exécution.
            - Si l'utilisateur a les permissions d'exécution, le script continue son exécution.
    """
    with contextlib.suppress(Exception):
        if sys.platform == "linux":
            excution_permission=subprocess.run(["bash", "permission.sh"])
            if excution_permission.returncode == 0:
                print("Permissions accordées")
            else:
                print("Permissions refusées")
                subprocess.run(["bash", "permission.sh"])

def define_os()->None:
    """
        Description: Cette fonction permet de définir l'OS sur lequel le script est exécuté.
            - Si le script est exécuté sur Linux, on lance le script de creation du service SemaWEB.
            - Si le script est exécuté sur Windows, on lance le script de creation du service SemaWEB.
        Paramètres: Aucun
        Retour: Aucun
    """
    if sys.platform == "linux":
        subprocess.run(["bash", "Services", "create_service.sh"])
    else:
        subprocess.run(["Services", "create_service.bat"])

def install_nmap()->None:
    """
        Description: Cette fonction permet d'installer Nmap sur Linux et windows.
        Paramètres: Aucun
        Retour: Aucun
    """
    if sys.platform == "linux":
        subprocess.run(["bash", "Services/Nmap/install_nmap.sh"])
    else:
        subprocess.run(["Services", "Nmap" ,"install_nmap.ps1"])

if __name__ == "__main__":
    define_permissions_linux()
    version_python()
    install_nmap()
    define_os()
    pre_installation()