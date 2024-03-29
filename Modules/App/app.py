#!/usr/bin/env python3.11.1

# Description: Fichier principal de l'application Semabox

"""
    Description: Fichier principal de l'application Semabox
        Ce script importe plusieurs modules Python nécessaires pour son fonctionnement. 
        Il importe également des fonctions de modules personnalisés se trouvant dans le répertoire 'Semabox/Modules'.
        Il définit une classe 'App' qui représente la fenêtre principale de l'application. 
        Le constructeur de cette classe initialise diverses variables telles que l'identifiant unique du système, le nom d'hôte, l'adresse IP et le nom de domaine associé. 
        Il configure également la fenêtre en lui attribuant un titre, une taille et un alignement au centre de l'écran. 
        Ensuite, il crée des widgets tels que des labels, des boutons et un menu déroulant. 
        Ces widgets sont placés dans la fenêtre et sont configurés avec des polices de caractères, des couleurs de fond, du texte et d'autres paramètres.
        Le script termine en exécutant la boucle principale de Tkinter pour afficher la fenêtre et rendre possible l'interaction avec l'utilisateur.
"""

# Importation des modules Pythons nécessaires
import contextlib  # Import du module 'contextlib'
import os  # Import du module 'os'
import tkinter as tk  # Import du module 'tkinter' pour l'interface graphique
import tkinter.font as tkFont  # Import du module 'tkFont' pour la gestion des polices de caractères
import platform  # Import du module 'platform' pour la gestion des plateformes(Windows, Linux, Mac)
from tkinter.ttk import *  # Import du module 'ttk' pour la gestion des widgets
from tkinter import (
    messagebox,
)  # Import du module 'messagebox' pour la gestion des messages d'alerte
from tkinter import *
import asyncio  # Import du module 'asyncio' pour la gestion des boucles asynchrones


# Importation des modules perso
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
# from Modules.generation_UID import lire_fichier, attribution_uid_variable  # Import des fonctions du module 'generation_UID'
from Registre.generationUID import Registres
from Information.info import InfoServer  # Import des fonctions du module 'info_server'
from Scan.scanPort import ScanPort  # Import de la fonction du module 'scan_servers'
from Speedtest.speedtest import (
    Speedtest,
)  # Import des fonctions du module 'server_speedtest'
from Serveur.update import Update  # Import de la fonction du module 'update_code'
from Scan.scanPortOtherServer import scan_port_other_machine
from Scan.scanAllServer import (
    ScanAllServer,
)  # Import de la fonction du module 'scan_port_other_servers'

# Création de la fenêtre principale (main window)
class App:
    # Constructeur de la classe App
    """
    Description:
        La classe App définit une application graphique utilisant l'interface utilisateur Tkinter.
        Le constructeur de la classe, __init__, prend en argument root, qui est la fenêtre principale de l'application.
        Le constructeur initialise plusieurs variables en appelant des fonctions de lecture de fichier, de récupération de nom d'hôte, d'adresse IP et de nom de domaine associé à l'adresse IP de l'hôte.
        Le constructeur configure également la fenêtre en définissant sa taille et son alignement au centre de l'écran, et en empêchant le redimensionnement par l'utilisateur.
        Enfin, le constructeur crée plusieurs widgets Tkinter pour afficher du texte et des couleurs de fond.
    """

    def __init__(self, root):
        """
        Fonction d'initialisation de la classe App:
            Description:
                Cette fonction initialise plusieurs variables en appelant des fonctions de lecture de fichier, de récupération de nom d'hôte, d'adresse IP et de nom de domaine associé à l'adresse IP de l'hôte.
                - ID: identifiant unique du système
                - host: nom d'hôte du système
                - ip: adresse IP du système
                - dns_resolv: nom de domaine associé à l'adresse IP du système
                - ping: variable initialisée à 0
                - self.ping: variable initialisée à 0
            Paramètres:
                root: fenêtre principale de l'application
                self: instance de la classe App
            Retour:
                Aucun

        """
        # Déclaration des variables

        ID = (
            Registres.lire_fichier()
        )  # On lit le fichier contenant l'identifiant unique généré par la fonction generate_id()
        host = (
            InfoServer.get_hostname()
        )  # On récupère le nom d'hôte (hostname) du système
        ip = InfoServer.get_ip_address()  # On récupère l'adresse IP de l'hôte
        dns_resolv = (
            InfoServer.get_dns()
        )  # On récupère le nom de domaine associé à l'adresse IP de l'hôte
        self.ping = 0  # On initialise la variable ping à 0

        # Configuration de la fenêtre
        root.title("Semabox")  # Titre de la fenêtre
        width = 1280  # Largeur de la fenêtre
        height = 720  # Hauteur de la fenêtre
        screenwidth = root.winfo_screenwidth()  # Largeur de l'écran
        screenheight = root.winfo_screenheight()  # Hauteur de l'écran
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )  # Alignement de la fenêtre au centre de l'écran
        root.geometry(
            alignstr
        )  # Affectation de la taille et de l'alignement de la fenêtre
        root.resizable(
            width=False, height=False
        )  # Empêche le redimensionnement de la fenêtre par l'utilisateur

        # Personalisation des polices de caractères
        font = tkFont.Font(family="Calibri", size=28, weight="bold")
        font2 = tkFont.Font(family="Calibri", size=17)
        font3 = tkFont.Font(family="Calibri", size=13)
        font4 = tkFont.Font(family="Calibri", size=20)
        font5 = tkFont.Font(family="Calibri", size=20, weight="bold")

        # Création des widgets

        # Titre de la fenêtre
        Titre_SEMABOX_Label = tk.Label(
            root,
            font=font,
            fg="#333333",
            bg="#ffd700",
            justify="center",
            relief="raised",
            text="SEMABOX",
        )
        Titre_SEMABOX_Label.place(x=0, y=0, width=1279, height=69)

        # Widget de la page d'accueil
        Texte_Information_Label = tk.Label(
            root,
            font=font5,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="INFORMATION",
        )
        Texte_Information_Label.place(x=940, y=90, width=339, height=41)

        # Widget Text : Donne les valeur associées à l'identifiant unique, l'adresse IP, le nom d'hôte et le nom de domaine associé à l'adresse IP
        Texte_IP_Label = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text=f"IP : {ip}",
        )
        Texte_IP_Label.place(x=940, y=130, width=339, height=30)

        Texte_DNS_Label = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text=f"DNS : {dns_resolv}",
        )
        Texte_DNS_Label.place(x=940, y=160, width=339, height=30)

        Texte_Hostname_Label = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text=f"Hostname : {host}",
        )
        Texte_Hostname_Label.place(x=940, y=190, width=338, height=31)

        Texte_Semabox_ID_Label = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text="SEMABOX UID :",
        )
        Texte_Semabox_ID_Label.place(x=940, y=220, width=339, height=151)

        Texte_Return_ID_Label = tk.Label(
            root, font=font3, fg="#333333", bg="#cdcdcd", justify="left", text=ID
        )
        Texte_Return_ID_Label.place(x=950, y=310, width=329, height=53)

        # Widget de la page de scan de port
        Texte_Scan_De_Port_Label = tk.Label(
            root,
            font=font5,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="SCAN DE PORT",
        )
        Texte_Scan_De_Port_Label.place(x=0, y=90, width=910, height=42)

        Texte_SPEEDTEST_Label = tk.Label(
            root,
            font=font5,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="SPEEDTEST",
        )
        Texte_SPEEDTEST_Label.place(x=940, y=400, width=339, height=41)

        # Widget Texte : Change en fonction lors du clique d'un bouton associer à une fonction
        self.Resultat_Scan_Nmap_Label = tk.Label(
            root, font=font4, fg="#333333", bg="#cdcdcd", justify="center", text=""
        )
        self.Resultat_Scan_Nmap_Label.place(x=0, y=130, width=722, height=587)

        self.Text_Label_Ping = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text="Ping : " + "" + " ms ",
        )
        self.Text_Label_Ping.place(x=940, y=440, width=338, height=46)
        self.update_ping_latency()

        self.Text_Label_Montant = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text="Débit Montant : " + "" + " mb/s",
        )
        self.Text_Label_Montant.place(x=940, y=480, width=339, height=48)

        self.Text_Label_Descendant = tk.Label(
            root,
            font=font2,
            fg="#333333",
            bg="#cdcdcd",
            justify="center",
            text="Débit Descendant : " + "" + " mb/s",
        )
        self.Text_Label_Descendant.place(x=940, y=520, width=338, height=51)

        # Widgets de couleur(fond)
        Color_Background5_Label = tk.Label(
            root, font=font, fg="#333333", bg="#393d49", justify="center", text=""
        )
        Color_Background5_Label.place(x=0, y=60, width=1279, height=30)

        Color_Background4_Label = tk.Label(
            root, font=font, fg="#333333", bg="#393d49", justify="center", text=""
        )
        Color_Background4_Label.place(x=910, y=90, width=30, height=626)

        Color_Background3_Label = tk.Label(
            root, font=font, fg="#333333", bg="#393d49", justify="center", text=""
        )
        Color_Background3_Label.place(x=940, y=370, width=339, height=30)

        Color_Background2_Label = tk.Label(
            root, font=font, fg="#333333", bg="#999999", justify="center", text=""
        )
        Color_Background2_Label.place(x=940, y=570, width=338, height=145)

        Color_Background_Label = tk.Label(
            root, font=font, fg="#333333", bg="#999999", justify="center", text=""
        )
        Color_Background_Label.place(x=720, y=130, width=191, height=586)

        # Boutons de l'interface
        Button_speedtest = tk.Button(
            root,
            font=font2,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="SPEEDTEST",
            command=lambda: asyncio.run(self.Button_speedtest_command()),
        )
        Button_speedtest.place(x=1050, y=610, width=125, height=40)

        Button_scan_nmap = tk.Button(
            root,
            font=font2,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="SCAN DE PORT",
            command=self.Button_scan_nmap_command,
        )
        Button_scan_nmap.place(x=740, y=380, width=150, height=36)

        Button_scan_nmap_machine = tk.Button(
            root,
            font=font2,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="SCAN DE MACHINE",
            command=self.Button_scan_nmap_machine,
        )
        Button_scan_nmap_machine.place(x=725, y=320, width=180, height=36)

        Button_clear_nmap = tk.Button(
            root,
            font=font2,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="CLEAR",
            command=self.Button_clear_nmap_command,
        )
        Button_clear_nmap.place(x=750, y=440, width=110, height=37)

        Button_speedtest_clear = tk.Button(
            root,
            font=font2,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="CLEAR",
            command=self.Button_speedtest_clear_command,
        )
        Button_speedtest_clear.place(x=1050, y=660, width=128, height=40)

        Button_scan_via_ip = tk.Button(
            root,
            font=font2,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="SCAN PORT IP",
            command=self.Button_scan_via_ip,
        )
        Button_scan_via_ip.place(x=740, y=220, width=150, height=36)

        #  Widgets de l'interface (Entry)
        self.tInput = Entry(root)
        self.tInput.place(x=740, y=180, width=150, height=30)

        self.Title_tInput = tk.Label(
            root,
            font=font3,
            fg="#333333",
            bg="#999999",
            justify="center",
            text="IP de votre Réseaux",
        )
        self.Title_tInput.place(x=740, y=140, width=150, height=30)

        # La ligne self.menu = tk.Menu(root) crée un menu tkinter et l'attribue à la variable self.menu.
        # Cela permet de créer un menu dans la fenêtre principale.
        self.menu = tk.Menu(root)

        # root.config(menu=self.menu) définit le menu créé à la ligne 1 comme menu pour la fenêtre principale.
        root.config(menu=self.menu)

        # Récupère le chemin absolu du fichier Python en cours d'exécution
        self.chemin_python = os.path.abspath(__file__)
        # Récupère le répertoire parent du fichier Python (qui est le répertoire de travail actuel)
        self.repertoire_travail = os.path.dirname(self.chemin_python)

        # Condition pour définir l'icône de la fenêtre principale et le thème de la fenêtre principale en fonction du système d'exploitation.
        if platform.system() == "Windows":
            file_path_icon = os.path.join(
                self.repertoire_travail, "assets/images/icons8_code.ico"
            )
            file_path_theme = os.path.join(
                self.repertoire_travail, "assets/themes/azure.tcl"
            )
            root.iconbitmap(file_path_icon)
            root.tk.call("source", file_path_theme)
        else:
            file_path_icon = os.path.join(
                self.repertoire_travail, "assets/images/code.png"
            )
            file_path_theme = os.path.join(
                self.repertoire_travail, "assets/themes/azure.tcl"
            )
            root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(file=file_path_icon))
            root.tk.call("source", file_path_theme)

        # root.tk.call("set_theme", "dark") définit le thème en noir pour l'instance Tk de la fenêtre principale
        root.tk.call("set_theme", "dark")

        # Création du menu "A propos"
        # self.help_menu crée un nouveau menu et l'attribue à la variable self.help_menu.
        self.help_menu = tk.Menu(self.menu)

        # self.menu.add_cascade ajoute une nouvelle cascade à self.menu avec l'étiquette "A propos" et assigne self.help_menu comme menu pour la cascade.
        self.menu.add_cascade(label="A propos", menu=self.help_menu)

        # self.help_menu.add_command crée une nouvelle commande avec l'étiquette "Update" dans self.help_menu et la commande est exécutée lorsque l'on clique sur "Update" .
        self.help_menu.add_command(label="Update", command=self.update_code)

        # self.help_menu.add_command crée une nouvelle commande avec l'étiquette "Version" dans self.help_menu et la commande est exécutée lorsque l'on clique sur "Version"
        self.help_menu.add_command(label="Version", command=self.about)

    def about(self):
        """
        Fonction : about
        Description : Fonction qui permet d'afficher la version de l'application
            def about(self): crée une nouvelle méthode appelée about et lorsqu'elle est appelée,
            elle affiche une boîte de message d'information avec le message "A propos" et
            la version de Ma Semabox en utilisant la fonction get_version_semabox()
        """
        messagebox.showinfo(
            "A propos", f"Version de Ma Semabox : {InfoServer.get_version_semabox()}"
        )

    def update_code(self):
        """
        Fonction : update_code
        Description : Fonction qui permet de vérifier si il y a une mise à jour de l'application
            def update_code(self): crée une nouvelle méthode appelée update_code et lorsqu'elle est appelée,
            elle affiche une boîte de message d'information avec le message "Update" et
            le status du code à l'aide de check_code_gitlab_application(get_latest_commit_date(os.getcwd()))
        """
        messagebox.showinfo("Update", Update.check_code_gitlab_application())

    # Fonction appelée lorsque le bouton "Button_scan_nmap" est cliqué
    def Button_scan_nmap_command(self):
        """
        Fonction: Button_scan_nmap_command
            Description : Permets de lancer le scan nmap et d'afficher les résultats dans le label
        """
        # Execution de la fonction "scan_nmap" et stockage du résultat dans la variable "result_scan"
        result_scan = ScanPort.scan()
        # Mise à jour du texte du label "Resultat_Scan_Nmap_Label" avec le contenu de la variable "result_scan"
        self.Resultat_Scan_Nmap_Label["text"] = result_scan

    def Button_scan_nmap_machine(self):
        """
        Fonction: Button_scan_nmap_machine
            Description : Permets de lancer le scan de machine et d'afficher les résultats dans le label
        """
        # Execution de la fonction "scan_nmap" et stockage du résultat dans la variable "result_scan"
        result_scan = ScanAllServer.cli_scan_machine()
        # Mise à jour du texte du label "Resultat_Scan_Nmap_Label" avec le contenu de la variable "result_scan"
        self.Resultat_Scan_Nmap_Label["text"] = result_scan

    async def Button_speedtest_command(self):
        """
        Fonction: Button_speedtest_command
            Description : Permets de lancer le speedtest et d'afficher les résultats dans les labels
        """

        # Appeler les fonctions asynchrones en parallèle avec `asyncio.gather`
        download_speed_task = asyncio.create_task(Speedtest.get_download_speed())
        upload_speed_task = asyncio.create_task(Speedtest.get_upload_speed())

        download_speed, upload_speed = await asyncio.gather(
            download_speed_task, upload_speed_task
        )

        # Mise à jour du texte du label "Text_Label_Montant" avec le contenu de la variable "download"
        self.Text_Label_Montant["text"] = f"Débit Montant : {download_speed} mb/s"
        # Mise à jour du texte du label "Text_Label_Descendant" avec le contenu de la variable "upload"
        self.Text_Label_Descendant["text"] = f"Débit Descendant : {upload_speed}  mb/s"

    # Fonction appelée lorsque le bouton "Button_clear_nmap" est cliqué
    def Button_clear_nmap_command(self):
        """
        Fonction: Button_clear_nmap_command
            Description : Effacer les résultats du Scan Nmap
        """
        # Mise à jour du texte du label "Resultat_Scan_Nmap_Label" avec une chaîne vide
        self.Resultat_Scan_Nmap_Label["text"] = ""

    # Fonction appelée lorsque le bouton "Button_speedtest_clear" est cliqué
    def Button_speedtest_clear_command(self):
        """
        Fonction: Button_speedtest_clear_command
            Description : Effacer les résultats du Speedtest
        """
        # Mise à jour du texte du label "Text_Label_Montant" avec la chaîne "Débit Montant : " suivie d'une chaîne vide suivie de " mb/s"
        self.Text_Label_Montant["text"] = "Débit Montant : " + "" + " mb/s"
        # Mise à jour du texte du label "Text_Label_Descendant" avec la chaîne "Débit Descendant : " suivie d'une chaîne vide suivie de " mb/s"
        self.Text_Label_Descendant["text"] = "Débit Descendant : " + "" + " mb/s"

    def update_ping_latency(self):

        """Fonction : update_ping_latency
        Description : Fonction qui permet de mettre à jour le ping
            - def update_ping_latency(self): crée une nouvelle méthode appelée update_ping_latency et lorsqu'elle est appelée,
              elle met à jour le ping dans le label "Text_Label_Ping" et relance la fonction après 1 seconde
            - self.ping = get_ping(): récupère le ping
            - self.Text_Label_Ping["text"] = f"PING : {self.ping} ms": met à jour le texte du label "Text_Label_Ping" avec le ping
            - root.after(1000, self.update_ping_latency): relance la fonction après 1 seconde
            - return: None
        Return: None
        Paramètres: None

        """

        self.ping = Speedtest.get_ping()
        self.Text_Label_Ping["text"] = f"PING : {self.ping} ms"
        root.after(1000, self.update_ping_latency)

    def getInputBoxValue(self):
        return self.tInput.get()

    def Button_scan_via_ip(self):
        """
        Fonction: Button_scan_via_ip
            Description : Permets de lancer le scan de machine et d'afficher les résultats dans le label
            Return: None
            Paramètres: None

        """
        result_scan2 = scan_port_other_machine(self.getInputBoxValue())
        self.Resultat_Scan_Nmap_Label["text"] = result_scan2
        self.clear_entry()

    def clear_entry(self):
        self.tInput.delete(0, END)


def verification_permission():
    """
    Fonction: verification_permission
        Description : Permets de vérifier si l'utilisateur est root
            - def verification_permission(): crée une nouvelle méthode appelée verification_permission
            - with contextlib.suppress(Exception): permet de supprimer les erreurs
            - if platform.system() == "Linux" and os.getuid() != 0: vérifie si l'utilisateur est root
            - print("Vous devez être root pour lancer cette application"): affiche un message d'erreur
        Return: None
        Paramètres: None
    """
    with contextlib.suppress(Exception):
        if platform.system() == "Linux" and os.getuid() != 0:
            print("Vous devez être root pour lancer cette application")


# Si le script est exécuté directement (et non importé par un autre script)
if __name__ == "__main__":

    # Vérification des permissions
    verification_permission()

    # Update du code
    Update.check_code_gitlab_application()

    # Création d'une instance de la classe Tk (fenêtre principale de l'application)
    root = tk.Tk()

    # Si la variable semabox_uid est vide
    if Registres.lire_fichier() == "":
        Registres.attribution_uid_variable()

    # Création d'une instance de la classe "App" avec en paramètre la fenêtre principale "root"
    app = App(root)

    # Lancement de la boucle principale de l'application
    root.mainloop()
