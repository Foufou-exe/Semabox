import dns.query
import dns.update
import sys

sys.path.append('Application')

from modules.info_server import get_ip_address, get_hostname

# domain : le nom de domaine auquel ajouter l'enregistrement
domain = 'cma4.box'
# ip : l'adresse IP de l'hôte à ajouter
ip = get_ip_address()
# enregistrement : le type d'enregistrement (A, AAAA, etc.)
enregistrement = 'A'
# ttl : le temps de vie (en secondes) de l'enregistrement
ttl = 300
# hostname : le nom de l'hôte à ajouter
hostname = get_hostname()
# serveur_dns : l'adresse IP du serveur DNS auquel envoyer la requête
serveur_dns = '192.168.100.253'

def addDnsRecord(domain, ip_dns, new_host, new_ip, enregistrement, ttl):
    # Créez un objet Update
    update = dns.update.Update(domain)
    # Ajoutez l'enregistrement de l'hôte
    update.add(new_host, ttl, enregistrement, new_ip)
    # Envoyez la requête DNS UPDATE
    response = dns.query.tcp(update, ip_dns)


if __name__ == "__main__":
    print(domain=domain, ip_dns=serveur_dns, host=hostname, new_ip=ip, enregistrement=enregistrement, ttl=ttl)