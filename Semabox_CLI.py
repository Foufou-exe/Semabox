#!/usr/bin/env python3.11.1
# Description: Ce fichier contient des fonctions permettant de récupérer des informations sur le serveur sur lequel le code est exécuté.

from pyfiglet import figlet_format
from prettytable import PrettyTable
import sys


# Importation des modules perso
sys.path.append('./SemaOS')  # On ajoute le chemin './SemaOS' au path de sys pour pouvoir importer les modules de ce répertoire
from info_server import cli_info_server
from materiel_server import cli_get_server_info
from scan_servers import scan_nmap
from server_speedtest import cli_speedtest
from latence import get_latency
from ping import get_ping


def afficher_menu():
    titre = figlet_format("Semabox CLI")
    print(titre)
    table = PrettyTable()
    table.field_names = ["Option", "Description"]
    table.add_row(["1", "Information Semabox"])
    table.add_row(["2", "Information Système"])
    table.add_row(["3", "Scan de Port"])
    table.add_row(["4", "Speedtest"])
    table.add_row(["5", "Ping + Latence"])
    print(table)
    


def menu():
    afficher_menu()
    choix = input("Entrez votre choix : ")
    if choix == "1":
        print(cli_info_server())

    elif choix == "2":

        print(cli_get_server_info())

    elif choix == "3":

        print(scan_nmap())

    elif choix == "4":

        print(cli_speedtest())

    elif choix == "5":

        print(f"Ping: {get_ping()} ms\nlatence: {get_latency()} ms")
    else:

        print("Choix non valide.")
        afficher_menu()

menu()