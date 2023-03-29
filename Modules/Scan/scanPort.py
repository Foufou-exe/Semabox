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
import nmap  # Pour scanner
import sys  # Pour ajouter le chemin du module info_server.py

# Ajout du chemin du module info_server.py
sys.path.append("Modules")
# Importation des modules Python personnalisés
from Information.info import InfoServer


class ScanPort:
    @staticmethod
    def scan() -> str:
        try:
            nm = nmap.PortScanner()  # Création d'un objet nmap.PortScanner()
            host = str(InfoServer.get_ip_address())  # Adresse IP de l'hôte à scanner
            nm.scan(
                host, arguments="-sS"
            )  # On scanne l'hôte en utilisant l'option -sS (SYN scan)
            result = ""  # Chaîne de caractères contenant les résultats du scan
            for host in nm.all_hosts():  # On parcourt tous les hôtes
                if nm[host].all_tcp():  # Si l'hôte a des ports ouverts
                    for port, info in nm[host][
                        "tcp"
                    ].items():  # On parcourt tous les ports ouverts
                        if info["state"] == "open":  # Si le port est ouvert
                            result += f"\nPort {port}/tcp | OPEN | service : {info['name']}"  # On ajoute les informations sur le port à la chaîne de caractères
                else:  # Si l'hôte n'a pas de ports ouverts
                    result += f"\nNo open TCP ports found on {host}"  # On ajoute les informations sur l'hôte à la chaîne de caractères
            return result  # Retourne une chaîne de caractères contenant les résultats du scan
        except KeyError as e:  # Erreur si l'hôte n'a pas de ports ouverts
            if e.args[0] == "tcp":
                return "Aucun Port ouvert"  # Retourne une chaîne de caractères contenant les résultats du scan

    @staticmethod
    def api_scan() -> dict:

        """
        Description:
            Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne un dictionnaire
            contenant les informations sur les ports ouverts.
        """
        try:
            # Création d'un objet nmap.PortScanner()
            nm = nmap.PortScanner()

            # Adresse IP de l'hôte à scanner
            host = str(InfoServer.get_ip_address())

            # On scanne l'hôte en utilisant l'option -sS (SYN scan)
            nm.scan(host, arguments="-sS")

            scan_results = {
                port: {"port": port, "state": data["state"], "service": data["name"]}
                for port, data in nm[host]["tcp"].items()
                if data["state"] == "open"
            }
            print(scan_results)

        except KeyError as e:
            if e.args[0] == "tcp":
                print({"message": "Aucun Port ouvert"})


# Si ce fichier est exécuté directement, on appelle la fonction api_scan()
if __name__ == "__main__":
    ScanPort.api_scan()
