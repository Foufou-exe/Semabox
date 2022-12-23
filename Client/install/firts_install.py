import csv
import sys
import os
import subprocess
sys.path.append("Client")
from modules.info_server import *
from modules.generation_UID import *

def premier_lancement():
    if not os.path.exists("SEMABOX_UID"):
        creation_dossier(generate_id())
    
    lire_fichier()
    


# def ecriture_fichier():
#     hostname = get_hostname()
#     ip = get_ip_address()
#     dns = get_dns(ip)
    
    
#     liste_info = [dns,hostname,ip,uid]
#     print(liste_info)
#     name_file = dns + ".csv"
#     # Création du fichier
#     fichier = f"Client/install/{name_file}"

#     with open(fichier, "wb") as outcsv:
#         writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         writer.writerows(liste_info)
    

if __name__ == "__main__":
    premier_lancement()