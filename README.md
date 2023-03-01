<div align="center">
  <h1>Projet Semabox 🖥️</h1>

  ![Logo](https://github.com/Foufou-exe/Semabox/blob/dev/.github/Logo_Banniere.png?raw=true)

  [![License Propriétaire](https://img.shields.io/badge/License-Propri%C3%A9taire-green.svg)](https://github.com/Foufou-exe/Semabox/blob/main/license)
  ![Version Python](https://img.shields.io/badge/Compatible-Python%203.11%203.10-yellow.svg)
  [![Documentation Status](https://readthedocs.org/projects/semabox/badge/?version=latest)](https://semabox.readthedocs.io/fr/latest/?badge=latest)

</div>

## Description

La Semabox est une sonde de surveillance de serveurs conçue pour effectuer des tests de débit, des scans de ports et des analyses de réseaux. Elle est intégrée aux serveurs pour surveiller en temps réel leur performance et leur sécurité.

### Les fonctionnalités de la Semabox incluent

- Détection de l'OS utilisé par le serveur
- Identification de l'IP publique et du nom d'hôte du serveur
- Analyse de la bande passante utilisée
- Scan de ports pour détecter les ports ouverts et les services en cours d'exécution
- Analyse de la sécurité réseau pour détecter les vulnérabilités potentielles

#### Toutes ces fonctionnalités sont gérées par des scripts Python appelés **SemaOS**

Les résultats de ces analyses peuvent être visualisés via une interface graphique, une ligne de commande ou une version web. Cela permet aux administrateurs de systèmes de surveiller facilement leur environnement de serveurs et de prendre des mesures pour résoudre les problèmes identifiés.

En résumé, la Semabox est un outil puissant pour surveiller la performance et la sécurité des serveurs, qui offre une vue d'ensemble complète des informations sur les serveurs surveillés et facilite la prise de décisions en matière de surveillance et de maintenance des serveurs.

## Installation Mode Manuel 👩‍🌾

Mise en situation :
*Les tests on était effectuer avec le compte root sous linux (**OS : Fedora**)*
*Le dossier Semabox à était git clone à la racine (**donc il a reçu des permissions**)*

Pour Windows, il n'y a aucune d'adaptation à faire

#### **Etape 1**: On clone le projet

```bash
git clone https://github.com/Foufou-exe/Semabox.git
```

#### **Etape 2**: Maintenant tu te rend dans le repertoire **install**

Commande : **Windows** && **Linux**

```bash
cd Semabox/install
```

#### **Etape 3** : On installe les librairies necessaires au bont fonctionnement de la Semabox

```bash
pip install -r requirement.txt
```

#### **Etape 4**: Pour Linux ,donner les permissions d'executions

Commande : **Linux**

```bash
dos2unix permission.sh
bash permission.sh
```

Si vous n'avez pas dos2unix , installer le `apt\yum\apk\dnf install dos2unix`

#### **Etape 5**: On installe les prérequis pour le bon fonctionnement de la Semabox

##### *Pour les Simples utilisateurs* :

```bash
python install_single_user.py
```

##### *Pour les entreprises* :

Penser à modifier le fichier **install_enterprise.py** dans la fonction `main()` :

```Python
  add_dns_record(
    domain='votre domaine',# domain : le nom de domaine auquel ajouter l'enregistrement
    ip_dns='IP de votre Serveur DNS', # serveur_dns : l'adresse IP du serveur DNS auquel envoyer la requête
    host=hostname(),# hostname : le nom de l'hôte à ajouter 
    new_ip=ip(), # ip : l'adresse IP de l'hôte à ajouter
    enregistrement='A', # enregistrement : le type d'enregistrement (A, AAAA, etc.)
    ttl=300 
  ) # ttl : le temps de vie (en secondes) de l'enregistrement

  add_bdd_record(
    sema_id=uid(), # uid : l'identifiant unique de la semabox
    sema_hostname=hostname(), # hostname : le nom de l'hôte de la semabox
    sema_ip=ip(),
    sema_ip_public=ip_public(), # ip_pubic : l'adresse IP publique de la semabox 
    sema_dns=dns_semabox(ip()), #+ "".join(".cma4.box") , # ip : l'adresse IP de la semabox
    sema_version=version_semabox(),  # version_semabox : la version de la semabox
    user='Utilsateur de votre BDD', # user : l'utilisateur de la base de données
    password='Le mot de passe associer', # password : le mot de passe de l'utilisateur
    host='IP BDD', # host : l'adresse IP du serveur de la base de données
    database='NOM DE LA BDD' # database : le nom de la base de données
  )

```

##### Commande à faire : 

```bash
python install_enterprise.py
```

#### L'installation est termine, vous pouvez retourner dans le dossier principal de la semabox et lance *Semabox.py* ( **si vous êtes sur Linux avec interfaces graphiques**) sinon lance *Semabox_CLI.py* pour **la version CLI** ou pour finir **la version Web**

Retour dans le dossier Principal :

```bash
cd ..
```

**Version Graphiques** :

```bash
python Semabox.py
```

![Logo](https://github.com/Foufou-exe/Semabox/blob/dev/.github/Semabox.png?raw=true)

**Version CLI** :

```bash
python Semabox_CLI.py
```

![Logo](https://github.com/Foufou-exe/Semabox/blob/dev/.github/Semabox_CLI.png?raw=true)

**Version Web** :

```bash
http://localhost:80/
```

![Logo](https://github.com/Foufou-exe/Semabox/blob/dev/.github/SemaWEB.png?raw=true)

## Installation Automatisée 🤖

Allez clonez le Projet Semabox Ansible et lisez le **README**

```bash
  git clone https://github.com/Foufou-exe/Semabox-Ansible.git
```

## Docker 🐳

Création du network (Changez le macvlan par bridge si vous êtes sur Windows ou Mac)

```docker
docker network -d macvlan Network_Semabox -o parent=eth0
```

Commande pour run l'image via le registre de docker

```docker
docker run -h semabox -dit --name semabox --network Network_Semabox --restart always -p 8080:80 -p 2222:22 -d semabox:2.0.0
```

Accès au container

```docker
docker exec -it semabox bash
```

Sinon utilisée le dockerfile qui se situe dans le projet sinon voici le code pour seulement avoir le dockerfile

```docker-compose.yml
version: '2.0'
services:
    semabox:
        container_name: semabox
        image: foufoudu34/semabox:latest
        restart: always
        ports:
            - '80:80'
            - '22:22'
        networks:
            - semabox

networks:
    semabox:
    # Changer macvlan par bridge si vous êtes sur Windows ou Mac OS car macvlan n'est pas supporté
    # Pour Windows, il faut aussi changer le driver_opts: parent: eth0 par parent: Ethernet
    # Pour Mac OS, il faut aussi changer le driver_opts: parent: eth0 par parent: en0
        driver: macvlan
        driver_opts:
            parent: eth0
        ipam:
            config:
                - subnet:
                     # Changer les valeurs par celle de votre réseau pour que le container soit dans le même réseau que votre machine
                    # Si vous êtes sur Windows ou Mac OS, mettez se que vous voulez, le container cominuquera avec votre machine via le port 80 mais il ne sera pas dans le même réseau
                    gateway: <votregateway>
                    ip_range: <votrevlan>
                    aux_addresses: <votrevlan>

```

## Support

En cas de problème, veuillez le signaler à cette adresse support@cma4.local .

## Auteur et Developpeur

#### L'entreprise Quadro

Developpeur :

- [@Dylan L](https://github.com/thorbeorn)
- [@Thibaut M](https://github.com/Foufou-exe) 
- [@Mathis L](https://github.com/mathislef34)
- [@Nicolas L](https://github.com/nicolasLlinares)

## License

[License Propriétaire](https://github.com/Foufou-exe/Semabox/blob/main/license)
