
import nmap
from modules.info_server import get_ip_address



def scan_nmap():
    
    # Création d'un objet nmap.PortScanner()
    nm = nmap.PortScanner()

    # Adresse IP de l'hôte à scanner
    host = get_ip_address()

    # On scanne l'hôte en utilisant l'option -sS (SYN scan)
    nm.scan(host, arguments='-sS')

    resultat_scan_list =  ""
    # Parcours des ports scanneés
    for port in nm[host]['tcp']:
        # Si le port est ouvert, affichage du nom du service associé
        if nm[host]['tcp'][port]['state'] == 'open':
            resultat_scan_list += f"\nPort {port}/tcp | OPEN | service : {nm[host]['tcp'][port]['name']}"
    return resultat_scan_list


