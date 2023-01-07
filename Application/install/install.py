# Description: Ce script permet d'installer la semabox sur le réseau local et de l'enregistrer dans la base de données.

"""
    Desciption:
      Ce script permet d'installer la semabox sur le réseau local et de l'enregistrer dans la base de données.

    Le script effectue les actions suivantes :

      Importe les modules Python nécessaires :
        Modules :  
          dns.query
          dns.update
          sys
          mysql.connector
        
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
import sys
import mysql.connector

# Ajout du chemin vers le dossier Application pour qu'on puisse importer nos modules
sys.path.append('Application')

# Importe de nos modules Python personnalisés
from modules.info_server import get_ip_address as ip, get_hostname as hostname, get_dns as dns, get_version_semabox as version_semabox
from modules.generation_UID import lire_fichier as uid

# Ajout d'un enregistrement DNS
def addDnsRecord(domain, ip_dns, new_host, new_ip, enregistrement, ttl):
  # Créez un objet Update
  update = dns.update.Update(domain)
  # Ajoutez l'enregistrement de l'hôte
  update.add(new_host, ttl, enregistrement, new_ip)
  # Envoyez la requête DNS UPDATE
  response = dns.query.tcp(update, ip_dns)



# Ajoutez un enregistrement à la table 'box' de la base de données 'semabox' sur le serveur MariaDB à l'adresse 192.168.150.250.
def addBddRecord(sema_id, sema_hostname, sema_ip, sema_dns, sema_version, user, password, host, database):
  
  # Connection à la base de données
  cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)

  # Création de l'objet curseur
  cursor = cnx.cursor()

  # Construction la déclaration INSERT
  insert_stmt = "INSERT INTO box (sema_id, sema_hostname, sema_ip, sema_dns, sema_version) VALUES (%s, %s, %s, %s, %s)"
  
  # TABLE box
  #     sema_id TEXT,
  #     sema_hostname VARCHAR(255) NOT NULL,
  #     sema_ip VARCHAR(20) NOT NULL,
  #     sema_dns VARCHAR(20) NOT NULL,
  #     sema_version VARCHAR(255) NOT NULL

  # Execution de la requête avec les valeurs à insérer dans la base de données
  cursor.execute(insert_stmt, (sema_id, sema_hostname, sema_ip, sema_dns, sema_version))

  # Enregistrez les modifications dans la base de données
  cnx.commit()

  # Fermez le curseur et la connexion
  cursor.close()
  cnx.close()



if __name__ == "__main__":
  # Appelle de la Focntion addDnsRecord :  Ajout de l'enregistrement DNS
  addDnsRecord(
    domain='cma4.box',# domain : le nom de domaine auquel ajouter l'enregistrement
    ip_dns='192.168.100.253', # serveur_dns : l'adresse IP du serveur DNS auquel envoyer la requête
    host=hostname(),# hostname : le nom de l'hôte à ajouter 
    new_ip=ip(), # ip : l'adresse IP de l'hôte à ajouter
    enregistrement='A', # enregistrement : le type d'enregistrement (A, AAAA, etc.)
    ttl=300 
  ) # ttl : le temps de vie (en secondes) de l'enregistrement
  
  # Appelle de la Focntion addBddRecord :  Insertion des données dans la base de données
  addBddRecord(
    sema_id=uid(), # uid : l'identifiant unique de la semabox
    sema_hostname=hostname(), # hostname : le nom de l'hôte de la semabox
    sema_ip=ip(), 
    sema_dns=dns(ip()), # ip : l'adresse IP de la semabox
    sema_version=version_semabox(),  # version_semabox : la version de la semabox
    user='semabox', # user : l'utilisateur de la base de données
    password='Mspr_epsi1!', # password : le mot de passe de l'utilisateur
    host='192.168.150.250', # host : l'adresse IP du serveur de la base de données
    database='semabox' # database : le nom de la base de données
  )

    
    