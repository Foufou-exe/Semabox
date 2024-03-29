#!/usr/bin/env python3.11.1

# Description: Ce script permet d'installer la semabox sur le réseau local et de l'enregistrer dans la base de données.

"""
    Le script effectue les actions suivantes :

      Importe les modules Python nécessaires :
        Modules :  
          dns.query
          dns.update
          sys
          mysql.connector
          subprocess
        
      Ajoute le chemin vers le dossier 'Application' afin de pouvoir importer nos modules Python personnalisés.
      
      Importe nos modules Python personnalisés :
        Fonctions:
          get_ip_address sous le nom ip
          get_hostname sous le nom hostname
          get_dns sous le nom dns
          get_version_semabox sous le nom version_semabox
          lire_fichier sous le nom uid
        
      Définit une fonction addDnsRecord() pour ajouter un enregistrement DNS :
        Variables :
          domain : le nom de domaine auquel ajouter l'enregistrement
          ip_dns : l'adresse IP du serveur DNS auquel envoyer la requête
          host : le nom de l'hôte à ajouter
          new_ip : l'adresse IP de l'hôte à ajouter
          enregistrement : le type d'enregistrement (A, AAAA, etc.)
          ttl : le temps de vie (en secondes) de l'enregistrement
      
      Définit une fonction addBddRecord() pour ajouter un enregistrement dans la table 'box' de la base de données 'semabox' sur le serveur MariaDB à l'adresse 192.168.150.250 :
        Variables :
          sema_id : l'ID de la semabox
          sema_hostname : le nom d'hôte de la semabox
          sema_ip : l'adresse IP de la semabox
          sema_dns : le DNS de la semabox
          sema_version : la version de la semabox
          user : le nom d'utilisateur à utiliser pour la connexion à la base de données
          password : le mot de passe à utiliser pour la connexion à la base de données
          host : le nom d'hôte/IP du serveur de base de données
          database : la base de données à laquelle se connecter
        
      Appelle la fonction addDnsRecord() pour ajouter un enregistrement DNS pour la semabox.
      
      Appelle la fonction addBddRecord() pour ajouter un enregistrement pour la semabox dans la table 'box' de la base de données 'semabox'.
  
"""
# Importation des modules Python nécessaires
import dns.query
import dns.update
import mysql.connector
import subprocess
import os
import sys
import ifaddr

# Importation de nos modules Python personnalisés qui se trouvent dans le dossier 'install'
import install_single_user

# Importe de nos modules Python personnalisés
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)  # Ajoute le chemin vers le dossier 'Semabox' afin de pouvoir importer nos modules Python personnalisés.
# Ajoute le chemin vers le dossier 'SemaOS' afin de pouvoir importer nos modules Python personnalisés.
# Importe nos modules Python personnalisés

from Modules import InfoServer
from Modules import generation_UID

# Définition des variables
ip = InfoServer.get_ip_address()
hostname = InfoServer.get_hostname()
dns_semabox = InfoServer.get_dns(ip)
version_semabox = InfoServer.get_version_semabox()
ip_public = InfoServer.get_public_ip()
uid = generation_UID.lire_fichier()


def get_ip_vpn() -> str:
    """
    Cette fonction permet de récupérer l'adresse IPv4 de l'interface "tun0" du système, qui est typiquement utilisée pour les connexions VPN.

    Retourne l'adresse IPv4 de l'interface "tun0" sous forme de chaîne de caractères.

    Si l'interface "tun0" n'est pas trouvée ou ne possède pas d'adresse IPv4, retourne None.

    Usage :
      ip_vpn = get_ip_vpn()
      if ip_vpn:
        print("L'adresse IPv4 de l'interface 'tun0' est :", ip_vpn)
      else:
        print("L'interface 'tun0' n'est pas trouvée ou ne possède pas d'adresse IPv4.")

    """

    # Récupère les informations sur les interfaces réseau configurées sur le système
    interfaces = ifaddr.get_adapters()

    # Parcourt la liste des interfaces pour trouver celle qui s'appelle "tun0"
    for interface in interfaces:
        if interface.nice_name == "tun0":
            # Récupère l'adresse IP de l'interface
            for ip in interface.ips:
                if ip.is_IPv4:
                    return ip.ip
            break


# Ajout d'un enregistrement DNS
def add_dns_record(domain, ip_dns, host, new_ip, enregistrement, ttl):
    """
    Description:
        Cette fonction ajoute un enregistrement DNS pour un nouvel hôte avec une adresse IP spécifiée dans le domaine spécifié.

    Args:
        domain (str): Le nom de domaine auquel ajouter l'enregistrement DNS.
        ip_dns (str): L'adresse IP du serveur DNS qui gère le domaine.
        new_host (str): Le nom de l'hôte à ajouter.
        new_ip (str): L'adresse IP de l'hôte à ajouter.
        enregistrement (str): Le type d'enregistrement DNS à ajouter (par exemple 'A', 'AAAA', 'CNAME', etc.).
        ttl (int): Le temps de vie de l'enregistrement DNS en secondes.
    """
    # Créez un objet Update
    update = dns.update.Update(domain)
    # Ajoutez l'enregistrement de l'hôte
    update.add(host, ttl, enregistrement, new_ip)
    # Envoyez la requête DNS UPDATE
    response = dns.query.tcp(update, ip_dns)

    # Vérifiez si la requête a réussi
    if response.rcode() == 0:
        print("Enregistrement DNS ajouté avec succès.")


# Ajoutez un enregistrement à la table 'box' de la base de données 'semabox' sur le serveur MariaDB à l'adresse 192.168.150.250.
def add_bdd_record(
    sema_id,
    sema_hostname,
    sema_ip,
    sema_ip_public,
    sema_dns,
    sema_version,
    user,
    password,
    host,
    database,
):
    """
    Description:
        Cette fonction ajoute un enregistrement à la table 'box' de la base de données 'semabox' sur le serveur MariaDB à l'adresse spécifiée.

    Args:
        sema_id (str): L'identifiant unique (UID) de l'installation de SemaOS.
        sema_hostname (str): Le nom d'hôte de l'installation de SemaOS.
        sema_ip (str): L'adresse IP de l'installation de SemaOS.
        sema_dns (str): Le nom de domaine de l'installation de SemaOS.
        sema_version (str): La version de SemaOS utilisée.
        user (str): Le nom d'utilisateur pour se connecter au serveur MariaDB.
        password (str): Le mot de passe pour se connecter au serveur MariaDB.
        host (str): L'adresse du serveur MariaDB.
        database (str): Le nom de la base de données à utiliser.
    """
    # Connection à la base de données
    cnx = mysql.connector.connect(
        user=user, password=password, host=host, database=database
    )

    # Création de l'objet curseur
    cursor = cnx.cursor()

    # Construction la déclaration INSERT
    insert_stmt = "INSERT INTO box (sema_id, sema_hostname, sema_ip, sema_ip_public, sema_dns, sema_version) VALUES (%s, %s, %s, %s, %s, %s)"

    # Execution de la requête avec les valeurs à insérer dans la base de données
    cursor.execute(
        insert_stmt,
        (sema_id, sema_hostname, sema_ip, sema_ip_public, sema_dns, sema_version),
    )

    # Enregistrez les modifications dans la base de données
    cnx.commit()

    # Fermez le curseur et la connexion
    cursor.close()
    cnx.close()


def get_uid():
    """
    Description:
        Cette fonction exécute le script de génération d'un identifiant unique (UID) pour l'installation de SemaOS.
    """
    # On se déplace dans le dossier parent
    file_path = os.path.join("..", "SemaOS", "generation_UID.py")
    subprocess.run(["python", file_path])


def main():
    """
    Description: Fonction principale du script
      - Appelle de la fonction creation_service_api() :  Permet de savoir sous quel système d'exploitation est installé le serveur et donc
      - Appelle de la fonction check_version_python() :  Vérifie la version de Python.
      - Appelle de la fonction define_permissions_linux() :  Définit les permissions Linux.
      - Appelle de la fonction Generation_UID() :  Exécute le script de génération d'un identifiant unique (UID) pour l'installation de SemaOS.
      - Appelle de la fonction add_dns_record() :  Ajoute un enregistrement DNS pour la semabox
      - Appelle de la fonction add_bdd_record() :  Insertion des données dans la base de données

    Paramètres:
      - les valeurs définies dans les fonctions peuvent être modifiées (adresse IP, nom de domaine, etc.)
    """
    install_single_user.permissions_linux()
    install_single_user.check_version_python()
    install_single_user.install_nmap()
    install_single_user.creation_service_api()
    get_uid()
    # Appelle de la Focntion add_dns_record :  Ajout de l'enregistrement DNS
    add_dns_record(
        domain="cma4.box",  # domain : le nom de domaine auquel ajouter l'enregistrement
        ip_dns="192.168.100.253",  # serveur_dns : l'adresse IP du serveur DNS auquel envoyer la requête
        host=hostname,  # hostname : le nom de l'hôte à ajouter
        new_ip=get_ip_vpn(),  # ip : l'adresse IP VPN de la semabox
        enregistrement="A",  # enregistrement : le type d'enregistrement (A, AAAA, etc.)
        ttl=300,
    )  # ttl : le temps de vie (en secondes) de l'enregistrement

    # Appelle de la Focntion add_bdd_record :  Insertion des données dans la base de données
    add_bdd_record(
        sema_id=uid,  # uid : l'identifiant unique de la semabox
        sema_hostname=hostname,  # hostname : le nom de l'hôte de la semabox
        sema_ip=get_ip_vpn(),  # ip : l'adresse IP VPN de la semabox
        sema_ip_public=ip_public,  # ip_pubic : l'adresse IP publique de la semabox
        sema_dns=dns_semabox
        + "".join(
            ".cma4.box"
        ),  # + "".join(".cma4.box") , # ip : l'adresse IP de la semabox
        sema_version=version_semabox,  # version_semabox : la version de la semabox
        user="semabox",  # user : l'utilisateur de la base de données
        password="Mspr_epsi1!",  # password : le mot de passe de l'utilisateur
        host="192.168.150.240",  # host : l'adresse IP du serveur de la base de données
        database="semabox",  # database : le nom de la base de données
    )


if __name__ == "__main__":
    main()
