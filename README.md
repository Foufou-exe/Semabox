<div align="center">
  <h1>Projet Semabox 🖥️</h1>

  ![Logo](https://raw.githubusercontent.com/Foufou-exe/Semabox/dev/Logo_Banniere.png?token=GHSAT0AAAAAAB4HK6L2IT7ENQKQUILJACO4Y6MBA7Q)


 
  
  [![License Propriétaire](https://img.shields.io/badge/License-Propri%C3%A9taire-green.svg)](https://github.com/Foufou-exe/Semabox/blob/main/license)
  ![Version Python](https://img.shields.io/badge/Compatible-Python%203.11.1-yellow.svg)

</div>

## Description

La Semabox est une sonde de surveillance de serveurs conçue pour effectuer des tests de débit, des scans de ports et des analyses de réseaux. Elle est intégrée aux serveurs pour surveiller en temps réel leur performance et leur sécurité.

### Les fonctionnalités de la Semabox incluent :

- Détection de l'OS utilisé par le serveur
- Identification de l'IP publique et du nom d'hôte du serveur
- Analyse de la bande passante utilisée
- Scan de ports pour détecter les ports ouverts et les services en cours d'exécution
- Analyse de la sécurité réseau pour détecter les vulnérabilités potentielles

#### Toutes ces fonctionnalités sont gérées par des scripts Python appelés **SemaOS**. 
Les résultats de ces analyses peuvent être visualisés via une interface graphique, une ligne de commande ou une version web. Cela permet aux administrateurs de systèmes de surveiller facilement leur environnement de serveurs et de prendre des mesures pour résoudre les problèmes identifiés.

En résumé, la Semabox est un outil puissant pour surveiller la performance et la sécurité des serveurs, qui offre une vue d'ensemble complète des informations sur les serveurs surveillés et facilite la prise de décisions en matière de surveillance et de maintenance des serveurs.

## Installation Mode Manuel 👩‍🌾

#### **Etape 1**: On clone le projet 

```bash
git clone https://github.com/Foufou-exe/Semabox.git
```
#### **Etape 2**: Maintenant tu te rend dans le repertoire **install** 

```bash
cd Semabox/install
```
#### **Etape 3**: On donne les permissions d'executer au scripts d'installation 

```bash
sudo chmod a+x *
```
### **Important**: *L'Etape 4* correspond à l'installation de **python 3.11.1** à faire si votre python n'est pas égale ou supperieur à cette version 


#### **Etape 4**: On lance **install_prerequis.sh** ( Installation de Python 3.11.1 )

```bash
sudo ./install_prerequis.sh
```

#### **Etape 5**: On installe les librairies necessaires au bont fonctionnement de la Semabox

```bash
pip install -r requirement.txt
```

#### **Etape 6**: On déplace le fichier Semabox-api.service dans /etc/systemd/system

```bash
mv Semabox-api.service /etc/systemd/system
```

#### **Etape 7**: On démarre le service et on l'active pour qu'il puisse redemarrer

```bash
systemctl start Semabox-api.service
systemctl enable Semabox-api.service
```

#### L'installation est termine, vous pouvez retourner dans le dossier principal de la semabox et lance *Semabox.py* ( **si vous êtes sur Linux avec interfaces graphiques**) sinon lance *Semabox_CLI.py* pour **la version CLI** ou pour finir **la version Web**.
Retour dans le dossier Principal :
```bash
cd ..
```
**Version Graphiques** :
```bash
python Semabox.py
```

**Version CLI** :
```bash
python Semabox_CLI.py
```

**Version Web** :
```bash
http://localhost:80/
```
## Installation Automatisée 🤖

Allez clonez le Projet Semabox Ansible et lisez le **README**

```bash
  git clone https://github.com/Foufou-exe/Semabox-Ansible.git
```

## Support

En cas de problème, veuillez le signaler à cette adresse support@cma4.local .



## Auteur et Developpeur

L'entreprise Quadro :

Developpeur : [@Dylan L](https://github.com/thorbeorn),[@Thibaut M](https://github.com/Foufou-exe) ,[@Mathis L](https://github.com/mathislef34),[@Nicolas L](https://github.com/nicolasLlinares) 



## License

[License Propriétaire](https://github.com/Foufou-exe/Semabox/blob/main/license)

