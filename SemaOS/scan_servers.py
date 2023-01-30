#!/usr/bin/env python3.11.1

# Description: Ce Script permet de scanner les ports ouverts sur l'hôte local.

"""
    Information:
        Importation des modules Python nécessaires:
            nmap - Ce module permet d'utiliser l'outil nmap en Python.

        Importation des modules Python personnalisés:
            info_server - Ce module contient la fonction get_ip_address() qui retourne l'adresse IP de l'hôte local.

        Fonctions:
            scan_nmap() - Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne une chaîne de caractères contenant les informations sur les ports ouverts.
            api_scan_nmap() - Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne un dictionnaire contenant les informations sur les ports ouverts.
"""

# Importation des modules Python nécessaires
import nmap
import sys

sys.path.append("SemaOS")
# Importation des modules Python personnalisés
from info_server import get_ip_address


# Fonctions
def scan_nmap() -> str:
    nm = nmap.PortScanner()
    host = get_ip_address()
    nm.scan(host, arguments='-sS')
    result = ''
    for host in nm.all_hosts():
        if nm[host].all_tcp():
            for port, info in nm[host]['tcp'].items():
                if info['state'] == 'open':
                    result += f"\nPort {port}/tcp | OPEN | service : {info['name']}"
        else:
            result += f"\nNo open TCP ports found on {host}"
    return result


def api_web_scan_nmap() -> dict:

    """
        Description:
            Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne un dictionnaire
            contenant les informations sur les ports ouverts.
    """
    
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = get_ip_address()

    # On scanne l'hôte en utilisant l'option -sS (SYN scan)
    nm.scan(host, arguments='-sS')

    scan_results = {
        port: {'port': port, 'state': data['state'], 'service': data['name']}
        for port, data in nm[host]['tcp'].items()
        if data['state'] == 'open'
    }
    return scan_results


def api_scan_nmap() -> dict:

    """
        Description:
            Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne un dictionnaire
            contenant les informations sur les ports ouverts.
    """
    
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = get_ip_address()

    # On scanne l'hôte en utilisant l'option -sS (SYN scan)
    nm.scan(host, arguments='-sS')

    scan_results = {
        port: {'port': port, 'state': data['state'], 'service': data['name']}
        for port, data in nm[host]['tcp'].items()
        if data['state'] == 'open'
    }
    print(scan_results)
    
def cli_get_scan_nmap() -> dict:

    """
        Description:
            Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne un dictionnaire
            contenant les informations sur les ports ouverts.
    """
    
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = get_ip_address()
    
    nm.scan(host, arguments='-sS')
    # On scanne l'hôte en utilisant l'option -sS (SYN scan)

    scan_results = {
        port: {'port': port, 'state': data['state'], 'service': data['name']}
        for port, data in nm[host]['tcp'].items()
        if data['state'] == 'open'
    }
    return scan_results

# Si ce fichier est exécuté directement, on appelle la fonction api_scan_nmap()
if __name__ == "__main__":
    print(cli_get_scan_nmap())
