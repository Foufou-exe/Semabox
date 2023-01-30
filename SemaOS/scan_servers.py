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
from SemaOS.info_server import get_ip_address


# Fonctions
def scan_nmap()->str:
    
    """
        Description:
            Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne une chaîne de caractères contenant les informations sur les ports ouverts.
    """
    
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = get_ip_address()

    # On scanne l'hôte en utilisant l'option -sS (SYN scan)
    nm.scan(host, arguments='-sS')
    
    port = None
    
    # On construit la chaîne de caractères à partir des informations sur les ports ouverts
    for host in nm.all_hosts():
        if nm[host].has_tcp(port):
            for port in nm[host]['tcp']:
                if nm[host]['tcp'][port]['state'] == 'open':
                    result += f"\nPort {port}/tcp | OPEN | service : {nm[host]['tcp'][port]['name']}"
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

    # On scanne l'hôte en utilisant l'option -sS (SYN scan)
    nm.scan(host, arguments='-sS')

    return {
        port: {'port': f'{port}/tcp', 'state': data['state'] + '✅', 'service': data['name']}
        for port, data in nm[host]['tcp'].items()
        if data['state'] == 'open'
    }

# Si ce fichier est exécuté directement, on appelle la fonction api_scan_nmap()
if __name__ == "__main__":
    api_scan_nmap()
