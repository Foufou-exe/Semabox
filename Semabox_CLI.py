#!/usr/bin/env python3.11.1
# Description: Ce fichier contient des fonctions permettant de récupérer des informations sur le serveur sur lequel le code est exécuté.

"""
    Description:
        Ce script utilise la bibliothèque pyfiglet pour créer un titre décoré, la bibliothèque prettytable pour afficher les informations de manière structurée et la bibliothèque termcolor pour mettre en couleur les informations affichées. 
        Il importe également des modules personnalisés pour récupérer les informations sur le serveur, comme cli_get_info_server, cli_get_info_system, cli_get_scan_nmap, cli_get_speedtest, cli_latence, cli_ping, scan_all_machine. 
        Le script contient également plusieurs fonctions pour afficher les informations récupérées dans un menu structuré et coloré. 
        Il utilise la fonction subprocess.run pour lancer des commandes système comme ping, nmap, speedtest. 
        Il utilise également des concepts de threading pour lancer certaines fonctions en arrière-plan comme cli_latence. 
        Il permet de scanner des machines dans un réseau local.
"""
# Importation des modules Python
from pyfiglet import figlet_format  # Permet de créer un titre décoré
from prettytable import PrettyTable # Permet d'afficher les informations de manière structurée sous forme de tableau
from termcolor import colored # Permet de mettre en couleur les informations affichées
import subprocess  # Permet d'exécuter des commandes système
import sys # Permet d'ajouter des chemins au path de sys
import ast # Permet de convertir une chaîne de caractères en dictionnaire
import platform # Permet de récupérer des informations sur le système
import os # Permet de récupérer des informations sur le système

# Importation des modules perso
sys.path.append('./SemaOS')  # On ajoute le chemin './SemaOS' au path de sys pour pouvoir importer les modules de ce répertoire
from info_server import cli_get_info_server
from materiel_server import cli_get_info_system
from scan_servers import cli_get_scan_nmap
from server_speedtest import cli_get_speedtest
from latence import cli_latence
from ping import cli_ping
from scan_other_servers import scan_all_machine


# Définition des fonctions
def afficher_menu():
    """
        Affiche un menu avec les différentes options disponibles
    """
    titre = figlet_format("Semabox CLI")
    print(titre)
    table = PrettyTable()
    table.field_names = [colored("Options","yellow"), colored("Fonctionnalités", "yellow")]
    table.add_row([colored("[", "green") + colored("1", "red") + colored("]", "green"), "Information Semabox"])
    table.add_row([colored("[", "green") + colored("2", "red") + colored("]", "green"), "Information Système"])
    table.add_row([colored("[", "green") + colored("3", "red") + colored("]", "green"), "Scan"])
    table.add_row([colored("[", "green") + colored("4", "red") + colored("]", "green"), "Speedtest"])
    table.add_row([colored("[", "green") + colored("5", "red") + colored("]", "green"), "Exit"])
    print(table)
    
def clear_screen():
    """
        Efface l'écran
    """
    system_name = platform.system()
    if system_name == "Windows":
        # do something specific for Windows
        os.system('cls')
    elif system_name == "Linux":
        # do something specific for Linux
        os.system('clear')
    else:
        print(f"Unsupported operating system: {system_name}")

def cli_info_server()->None:
    """
        Affiche les informations du serveur
    """
    info = cli_get_info_server()
    info_table = PrettyTable()
    info_table.field_names = [colored("Information","yellow"), colored("Valeurs", "yellow")]
    for key, value in info.items():
        info_table.add_row([colored(key, "green"), colored(value, "red")])
    print('\n')
    print(info_table)
    

def cli_materiel()->None:
    """
        Affiche les informations sur le matériel
    """
    materiel = cli_get_info_system()
    materiel_table = PrettyTable()
    materiel_table.field_names = [colored("Information","yellow"), colored("Valeurs", "yellow")]
    for key, value in materiel.items():
        materiel_table.add_row([colored(key, "green"), colored(value, "red")])
    print('\n')
    print(materiel_table)

def cli_scan()->None:
    """
        Affiche les informations sur le scan de ports de la machine
    """
    scan = cli_get_scan_nmap()
    scan_table = PrettyTable()
    scan_table.field_names = [colored("Port","yellow"), colored("Etat", "yellow"), colored("Service", "yellow")]
    for key ,value in scan.items():
        scan_table.add_row([colored(value['port'], "blue"), colored(value['state'], "white"), colored(value['service'], "red")])
    print('\n')
    print(scan_table)
    
def cli_speedtest()->None:
    """
        Affiche les informations sur le speedtest de la machine
    """
    speedtest = cli_get_speedtest()
    speedtest_table = PrettyTable()
    speedtest_table.field_names = [colored("Information","yellow"), colored("Valeurs", "yellow")]
    for key, value in speedtest.items():
        speedtest_table.add_row([colored(key, "blue"),colored(value, "red")])
    print('\n')
    print(speedtest_table)

def cli_scan_all_machine() -> None:
    """
        Affiche les informations sur des scans de ports de machines dans un réseau local
    """
    scan = scan_all_machine()
    scan_table = PrettyTable()
    scan_table.field_names = [colored("IP","yellow"), colored("Hostname", "yellow"), colored("Etat", "yellow")]
    for key, value in scan.items():
        scan_table.add_row([colored(value['host'], "blue"), colored(value['hostname'], "white"), colored(value['state'], "green")])
    print('\n')
    print(scan_table)

def cli_scan_port_machine():
    """
        Scans les ports d'une machine donnée en entrée, affiche les résultats dans un tableau et demande à l'utilisateur s'il souhaite scanner une nouvelle machine
    """
    reponse = input(colored("Veuillez entrer l'adresse IP de la machine à scanner (exemple: 192.168.1.1): ", "yellow"))
    results = subprocess.run(['python', f'./SemaOS/scan_port_other_servers.py','--ip',reponse], stdout=subprocess.PIPE)
    outputs = results.stdout.decode('utf-8')
    disctionnaires = ast.literal_eval(outputs)
    scan_machine_table = PrettyTable()
    scan_machine_table.field_names = [colored("Port","yellow"), colored("Etat", "yellow"), colored("Service", "yellow")]
    for key ,value in disctionnaires.items():
        scan_machine_table.add_row([colored(value['port'], "blue"), colored(value['state'], "white"), colored(value['service'], "red")])
    print('\n')
    print(scan_machine_table)
    reponse_new = input(colored("Est-ce que vous voulez scanenr une nouvelle machine ?", "yellow") + (colored("[", "white")) + (colored("O", "green")) + (colored("/", "white")) + (colored("N", "red")) + colored("]", "white") + ": ")
    if reponse_new in ["O", "o"]:
        cli_scan_port_machine()
    elif reponse_new in ["N", "n"]:
        menu()

def choix_menu() -> str:
    """
        Demande à l'utilisateur s'il souhaite continuer et redirige vers le menu principal ou quitte le programme
    """
    reponse = input(colored("Voulez-vous continuer ?", "yellow") + (colored("[", "white")) + (colored("O", "green")) + (colored("/", "white")) + (colored("N", "red")) + colored("]", "white") + ": ")
    if reponse in ["O", "o"]:
        clear_screen()
        menu()
    elif reponse in ["N", "n"]:
        clear_screen()
        print(colored("Au revoir !", "red"))
        sys.exit()
    else:
        clear_screen()
        print("Choix non valide.")
        choix_menu()
        
def choix_menu_scan() -> str:
    """
        Affiche un menu avec les différentes options de scan disponibles
    """
    table_scan = PrettyTable()
    table_scan.field_names = [colored("Options","yellow"), colored("Fonctionnalités", "yellow")]
    table_scan.add_row([colored("[", "green") + colored("1", "red") + colored("]", "green"), "Scan de Port de la Semabox"])
    table_scan.add_row([colored("[", "green") + colored("2", "red") + colored("]", "green"), "Scan complet du réseau local"])
    table_scan.add_row([colored("[", "green") + colored("3", "red") + colored("]", "green"), "Scan de Port d'une machine du réseau local"])
    table_scan.add_row([colored("[", "green") + colored("4", "red") + colored("]", "green"), "Retour au menu principal"])
    table_scan.add_row([colored("[", "green") + colored("5", "red") + colored("]", "green"), "Exit"])
    clear_screen()
    print(table_scan)
         
def menu()->None:
    """
        Affiche un menu avec les différentes options disponibles et permet à l'utilisateur de choisir une option pour effectuer une action spécifique.
    """
    clear_screen()
    afficher_menu()
    print("\n")
    choix = input(colored("Entrez votre choix entre ", "yellow") + (colored("[", "white")) + (colored("1", "red")) + (colored("-", "white")) + (colored("5", "red")) + colored("]", "white") + ": ") 
    if choix == "1":
        clear_screen()
        cli_info_server()
        choix_menu()

    elif choix == "2":
        clear_screen()
        cli_materiel()
        choix_menu()

    elif choix == "3":
        choix_menu_scan()
        choix_scan = input(colored("Entrez votre choix entre ", "yellow") + (colored("[", "white")) + (colored("1", "red")) + (colored("-", "white")) + (colored("5", "red")) + colored("]", "white") + ": ")
        if choix_scan == "1":
            cli_scan()
            choix_menu()
        elif choix_scan == "2":
            cli_scan_all_machine()
            choix_menu()
        elif choix_scan == "3":
            cli_scan_all_machine()
            cli_scan_port_machine()
        elif choix_scan == "4":
            print(colored("Au revoir !", "red"))
            sys.exit()
        else:
            clear_screen()
            print("Choix non valide.")
            choix_menu_scan()

    elif choix == "4":
        clear_screen()
        cli_speedtest()
        choix_menu()
        
    elif choix == "5":
        clear_screen()
        print(colored("Au revoir !", "red"))
        sys.exit()
    else:
        clear_screen()
        print("Choix non valide.")
        afficher_menu()
        
        

if __name__ == "__main__":
    menu()

