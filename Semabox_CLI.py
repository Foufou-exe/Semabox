#!/usr/bin/env python3.11.1
# Description: Ce fichier contient des fonctions permettant de récupérer des informations sur le serveur sur lequel le code est exécuté.

from pyfiglet import figlet_format
from prettytable import PrettyTable
from termcolor import colored
import sys
import time


# Importation des modules perso
sys.path.append('./SemaOS')  # On ajoute le chemin './SemaOS' au path de sys pour pouvoir importer les modules de ce répertoire
from info_server import cli_get_info_server
from materiel_server import cli_get_info_system
from scan_servers import cli_get_scan_nmap
from server_speedtest import cli_get_speedtest
from latence import cli_latence
from ping import cli_ping


def afficher_menu():
    titre = figlet_format("Semabox CLI")
    print(titre)
    table = PrettyTable()
    table.field_names = [colored("Options","yellow"), colored("Fonctionnalités", "yellow")]
    table.add_row([colored("[", "green") + colored("1", "red") + colored("]", "green"), "Information Semabox"])
    table.add_row([colored("[", "green") + colored("2", "red") + colored("]", "green"), "Information Système"])
    table.add_row([colored("[", "green") + colored("3", "red") + colored("]", "green"), "Scan de Port"])
    table.add_row([colored("[", "green") + colored("4", "red") + colored("]", "green"), "Speedtest"])
    table.add_row([colored("[", "green") + colored("5", "red") + colored("]", "green"), "Ping + Latence"])
    table.add_row([colored("[", "green") + colored("6", "red") + colored("]", "green"), "Exit"])
    print(table)
    
def cli_info_server()->None:
    info = cli_get_info_server()
    info_table = PrettyTable()
    info_table.field_names = [colored("Information","yellow"), colored("Valeurs", "yellow")]
    for key, value in info.items():
        info_table.add_row([colored(key, "green"), colored(value, "red")])
    print('\n')
    print(info_table)
    

def cli_materiel()->None:
    materiel = cli_get_info_system()
    materiel_table = PrettyTable()
    materiel_table.field_names = [colored("Information","yellow"), colored("Valeurs", "yellow")]
    for key, value in materiel.items():
        materiel_table.add_row([colored(key, "green"), colored(value, "red")])
    print('\n')
    print(materiel_table)

def cli_scan()->None:
    scan = cli_get_scan_nmap()
    scan_table = PrettyTable()
    scan_table.field_names = [colored("Port","yellow"), colored("Etat", "yellow"), colored("Service", "yellow")]
    for key ,value in scan.items():
        scan_table.add_row([colored(value['port'], "blue"), colored(value['state'], "white"), colored(value['service'], "red")])
    print('\n')
    print(scan_table)
    
def cli_speedtest()->None:
    speedtest = cli_get_speedtest()
    speedtest_table = PrettyTable()
    speedtest_table.field_names = [colored("Information","yellow"), colored("Valeurs", "yellow")]
    for key, value in speedtest.items():
        speedtest_table.add_row([colored(key, "blue"),colored(value, "red")])
    print('\n')
    print(speedtest_table)


def cli_ping_latence() -> None:
    while True:
        ping = cli_ping()
        latency = cli_latence()
        ping_table = PrettyTable()
        ping_table.clear_rows()

        ping_table.field_names = [colored("Ping","yellow"), colored("Latence", "yellow")]
        for key, value in ping.items():
            for key, values in latency.items():
                ping_table.add_row([colored(f"{value} ms", "blue"),colored(f"{values} ms", "red")])
        
        print('\n')
        print(ping_table)
    
    
def choix_menu() -> str:
    reponse = input(colored("Voulez-vous continuer ?", "yellow") + (colored("[", "white")) + (colored("O", "green")) + (colored("/", "white")) + (colored("N", "red")) + colored("]", "white") + ": ")
    if reponse in ["O", "o"]:
        menu()
    elif reponse in ["N", "n"]:
        print(colored("Au revoir !", "red"))
        sys.exit()
    else:
        print("Choix non valide.")
        choix_menu()
        
        
         
def menu()->None:
    afficher_menu()
    print("\n")
    choix = input(colored("Entrez votre choix entre ", "yellow") + (colored("[", "white")) + (colored("1", "red")) + (colored("-", "white")) + (colored("6", "red")) + colored("]", "white") + ": ") 
    if choix == "1":
        cli_info_server()
        choix_menu()

    elif choix == "2":
        cli_materiel()
        choix_menu()

    elif choix == "3":
        cli_scan()
        choix_menu()

    elif choix == "4":
        cli_speedtest()
        choix_menu()

    elif choix == "5":
        cli_ping_latence()
        choix_menu()
        
    elif choix == "6":
        print(colored("Au revoir !", "red"))
        sys.exit()
    else:
        print("Choix non valide.")
        afficher_menu()
        
        

if __name__ == "__main__":
    menu()

