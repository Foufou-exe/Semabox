#!/usr/bin/env python3.11.1

# Description: Ce Script permet de scanner les ports ouverts sur l'hôte local.



def scan_all_machine(network=get_address_network())->dict:
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = str(network)

    # On scanne l'hôte en utilisant l'option -sP (Ping scan)
    nm.scan(host, arguments='-sP')
    
    scan_results = {
        host: {"host": host,"hostname" : nm[host].hostname() ,"state": nm[host].state()}
        for host in nm.all_hosts()
        if nm[host].state() == 'up'
    } 
    
    return scan_results # Retourne un dictionnaire contenant les résultats du scan

def api_scan_machine(network=get_address_network())->dict:
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = str(network)

    # On scanne l'hôte en utilisant l'option -sP (Ping scan)
    nm.scan(host, arguments='-sP')
    
    scan_results = {
        host: {"host": host,"hostname" : nm[host].hostname() ,"state": nm[host].state()}
        for host in nm.all_hosts()
        if nm[host].state() == 'up'
    }
    
    print(scan_results) # Affiche les résultats du scan
    
def cli_scan_machine()->str:
    return "".join(
        f"\n La Machine {machine['hostname']} en {machine['host']}  est {machine['state']}"
        for machine in scan_all_machine().values()
    ) # Retourne une chaîne de caractères contenant les résultats du scan
    
if __name__ == "__main__":
    api_scan_machine()