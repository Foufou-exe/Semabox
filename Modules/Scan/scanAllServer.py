#!/usr/bin/env python3.11.1

# Description: Ce Script permet de scanner les ports ouverts sur l'hôte local.

# Importation des modules Python nécessaires
import nmap # Pour scanner les ports
import sys 

# Ajoute le chemin d'accès au module generation_UID.py
sys.path.append("Modules")

from Information.info import InfoServer

class ScanAllServer:
    
    @staticmethod
    def scan_machines() -> dict:
        """
        Description: Fonction qui scanne les machines connectées au réseau local.
            - Le scan est effectué en utilisant l'option -sP (Ping scan) de nmap.
            - Le scan est effectué sur le réseau local de la machine sur laquelle le code est exécuté.
        Returns:
            dict : dictionnaire contenant les résultats du scan
        """
        # Création d'un objet nmap.PortScanner()
        nm = nmap.PortScanner()

        # Adresse IP de l'hôte à scanner
        host = str(InfoServer.get_ip_address())

        # On scanne l'hôte en utilisant l'option -sP (Ping scan)
        nm.scan(host, arguments='-sP')

        scan_results = {
            host: {"host": host,"hostname" : nm[host].hostname() ,"state": nm[host].state()}
            for host in nm.all_hosts()
            if nm[host].state() == 'up'
        } 

        return scan_results # Retourne un dictionnaire contenant les résultats du scan
    
    @staticmethod
    def api_scan_machines() -> dict:
        """
        Description: Fonction qui scanne les machines connectées au réseau local.
            - Le scan est effectué en utilisant l'option -sP (Ping scan) de nmap.
            - Le scan est effectué sur le réseau local de la machine sur laquelle le code est exécuté.
        Returns:
            dict : dictionnaire contenant les résultats du scan
        """
        scan_results = ScanAllServer.scan_machines()
        print(scan_results) # Affiche les résultats du scan
        return scan_results
        
    @staticmethod
    def cli_scan_machine() -> str:
        """
            Description: Fonction qui scanne les machines connectées au réseau local.
                - Le scan est effectué en utilisant l'option -sP (Ping scan) de nmap.
                - Le scan est effectué sur le réseau local de la machine sur laquelle le code est exécuté.
            Returns:
                str : chaîne de caractères contenant les résultats du scan
            Parameters:
                network (str) : adresse de réseau
        """
        scan_results = ScanAllServer.scan_machines()
        return "".join(
            f"\n La Machine {machine['hostname']} en {machine['host']}  est {machine['state']}"
            for machine in scan_results.values()
        ) # Retourne une chaîne de caractères contenant les résultats du scan
        
if __name__ == "__main__":
    print(ScanAllServer.cli_scan_machine())