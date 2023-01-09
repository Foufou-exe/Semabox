import os
from info_server import get_ip_address

def server_is_up(host):
    response = os.system(f"ping {host}")
    return response == 0

if server_is_up(get_ip_address()):
    resultat1 = {"etat": "up"}
    return resultat1
else:
   resultat2 = {"etat": "down"}
   return resultat2