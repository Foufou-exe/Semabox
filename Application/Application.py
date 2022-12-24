# Importation des modules
import tkinter as tk
import tkinter.font as tkFont
import os

# Importation des modules perso
from modules.generation_UID import lire_fichier, creation_dossier, generate_id
from modules.info_server import *
from modules.scan_servers import scan_nmap
from modules.server_speedtest import get_upload_speed, get_download_speed , get_ping


# Création de la fenêtre principale (main window)
class App:
    # Constructeur de la classe App
    def __init__(self, root):
        # Déclaration des variables 
        ID = lire_fichier()
        host = get_hostname()
        ip = get_ip_address()
        dns_resolv = get_dns(ip)
        
        #setting title
        root.title("Semabox")
        #setting window size
        width=1280
        height=720
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # Création des widgets
        font = tkFont.Font(family='Calibri', size=28, weight='bold')
        font2 = tkFont.Font(family='Calibri', size=17)
        font3 = tkFont.Font(family='Calibri', size=13)
        font4 = tkFont.Font(family='Calibri', size=20)
        font5 = tkFont.Font(family='Calibri', size=20, weight='bold')
        
        Titre_SEMABOX_Label=tk.Label(root, font=font ,fg="#333333" ,bg="#ffd700" ,justify="center" ,relief="raised" ,text="SEMABOX")
        Titre_SEMABOX_Label.place(x=0,y=0,width=1279,height=69)

        Color_Background5_Label=tk.Label(root, font=font ,fg="#333333" ,bg="#393d49" ,justify="center" ,text="")
        Color_Background5_Label.place(x=0,y=60,width=1279,height=30)

        Color_Background4_Label=tk.Label(root, font=font ,fg="#333333" ,bg="#393d49" ,justify="center" ,text="")
        Color_Background4_Label.place(x=910,y=90,width=30,height=626)

        Color_Background3_Label=tk.Label(root, font=font ,fg="#333333" ,bg="#393d49" ,justify="center" ,text="")
        Color_Background3_Label.place(x=940,y=370,width=339,height=30)

        Texte_Information_Label=tk.Label(root, font=font5 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="INFORMATION")
        Texte_Information_Label.place(x=940,y=90,width=339,height=41)

        Texte_IP_Label=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text=f"IP : {ip}")
        Texte_IP_Label.place(x=940,y=130,width=339,height=30)

        Texte_DNS_Label=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text=f"DNS : {dns_resolv}")
        Texte_DNS_Label.place(x=940,y=160,width=339,height=30)

        Texte_Hostname_Label=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text=f"Hostname : {host}")
        Texte_Hostname_Label.place(x=940,y=190,width=338,height=31)

        Texte_Semabox_ID_Label=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text="SEMABOX UID :")
        Texte_Semabox_ID_Label.place(x=940,y=220,width=339,height=151)

        Texte_Return_ID_Label=tk.Label(root, font=font3 ,fg="#333333" ,bg="#cdcdcd" ,justify="left" ,text=ID)
        Texte_Return_ID_Label.place(x=950,y=310,width=329,height=53)

        Texte_Scan_De_Port_Label=tk.Label(root, font=font5 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="SCAN DE PORT")
        Texte_Scan_De_Port_Label.place(x=0,y=90,width=910,height=42)

        Texte_SPEEDTEST_Label=tk.Label(root, font=font5 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="SPEEDTEST")
        Texte_SPEEDTEST_Label.place(x=940,y=400,width=339,height=41)

        self.Resultat_Scan_Nmap_Label=tk.Label(root, font=font4 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text="")
        self.Resultat_Scan_Nmap_Label.place(x=0,y=130,width=722,height=587)

        Color_Background_Label=tk.Label(root, font=font ,fg="#333333" ,bg="#999999" ,justify="center" ,text="")
        Color_Background_Label.place(x=720,y=130,width=191,height=586)

        Button_scan_nmap=tk.Button(root, font=font2 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="SCAN" ,command=self.Button_scan_nmap_command)
        Button_scan_nmap.place(x=770,y=380,width=107,height=36)


        self.Text_Label_Ping=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text="PING :" + "" + " ms")
        self.Text_Label_Ping.place(x=940,y=440,width=338,height=46)

        self.Text_Label_Montant=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text="Débit Montant : " + "" + " mb/s")
        self.Text_Label_Montant.place(x=940,y=480,width=339,height=48)

        self.Text_Label_Descendant=tk.Label(root, font=font2 ,fg="#333333" ,bg="#cdcdcd" ,justify="center" ,text="Débit Descendant : " + "" + " mb/s")
        self.Text_Label_Descendant.place(x=940,y=520,width=338,height=51)

        Color_Background2_Label=tk.Label(root, font=font ,fg="#333333" ,bg="#999999" ,justify="center" ,text="")
        Color_Background2_Label.place(x=940,y=570,width=338,height=145)

        Button_speedtest=tk.Button(root, font=font2 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="SPEEDTEST" ,command=self.Button_speedtest_command)
        Button_speedtest.place(x=1050,y=610,width=125,height=40)

        
        Button_clear_nmap=tk.Button(root, font=font2 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="CLEAR" ,command=self.Button_clear_nmap_command)
        Button_clear_nmap.place(x=770,y=440,width=110,height=37)

        Button_speedtest_clear=tk.Button(root, font=font2 ,fg="#333333" ,bg="#999999" ,justify="center" ,text="CLEAR" ,command=self.Button_speedtest_clear_command)
        Button_speedtest_clear.place(x=1050,y=660,width=128,height=40)

    def Button_scan_nmap_command(self):
        result_scan = scan_nmap()
        self.Resultat_Scan_Nmap_Label["text"] = result_scan


    def Button_speedtest_command(self):
        ping = get_ping()
        download = get_download_speed()
        upload = get_upload_speed()
        
        self.Text_Label_Ping["text"] = f"PING : {ping} ms"
        self.Text_Label_Montant["text"] = f"Débit Montant : {download} mb/s"
        self.Text_Label_Descendant["text"] = f"Débit Descendant : {upload}  mb/s"
        
    def Button_clear_nmap_command(self):
        self.Resultat_Scan_Nmap_Label["text"] = ""


    def Button_speedtest_clear_command(self):
        self.Text_Label_Ping["text"] = "PING :" + "" + " ms"
        self.Text_Label_Montant["text"] = "Débit Montant : " + "" + " mb/s"
        self.Text_Label_Descendant["text"] = "Débit Descendant : " + "" + " mb/s"
        

        
if __name__ == "__main__":
    root = tk.Tk()
    if not os.path.exists("SEMABOX_UID"):
        # Création du dossier UID
        creation_dossier(generate_id())
    app = App(root)
    root.mainloop()




