# Importation des modules
import tkinter as tk
import tkinter.font as tkFont
from modules.generation_UID import lire_fichier
from modules.info_server import *
from modules.scan_servers import scan_nmap
from modules.server_speedtest import get_upload_speed, get_download , get_ping

# Déclaration des variables 
ID = lire_fichier()
host = get_hostname()
ip = get_ip_address()
dns_resolv = get_dns(ip)


# Création de la fenêtre principale (main window)
class App:
    # Constructeur de la classe App
    def __init__(self, root):
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
        Titre_SEMABOX_Label=tk.Label(root)
        Titre_SEMABOX_Label["bg"] = "#ffd700"
        ft = tkFont.Font(family='Calibri',size=28)
        Titre_SEMABOX_Label["font"] = ft
        Titre_SEMABOX_Label["fg"] = "#333333"
        Titre_SEMABOX_Label["justify"] = "center"
        Titre_SEMABOX_Label["text"] = "SEMABOX"
        Titre_SEMABOX_Label["relief"] = "raised"
        Titre_SEMABOX_Label.place(x=0,y=0,width=1279,height=69)

        Color_Background5_Label=tk.Label(root)
        Color_Background5_Label["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=10)
        Color_Background5_Label["font"] = ft
        Color_Background5_Label["fg"] = "#333333"
        Color_Background5_Label["justify"] = "center"
        Color_Background5_Label["text"] = ""
        Color_Background5_Label.place(x=0,y=60,width=1279,height=30)

        Color_Background4_Label=tk.Label(root)
        Color_Background4_Label["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=10)
        Color_Background4_Label["font"] = ft
        Color_Background4_Label["fg"] = "#333333"
        Color_Background4_Label["justify"] = "center"
        Color_Background4_Label["text"] = ""
        Color_Background4_Label.place(x=910,y=90,width=30,height=626)

        Color_Background3_Label=tk.Label(root)
        Color_Background3_Label["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=12)
        Color_Background3_Label["font"] = ft
        Color_Background3_Label["fg"] = "#333333"
        Color_Background3_Label["justify"] = "center"
        Color_Background3_Label["text"] = ""
        Color_Background3_Label.place(x=940,y=370,width=339,height=30)

        Texte_Information_Label=tk.Label(root)
        Texte_Information_Label["anchor"] = "center"
        Texte_Information_Label["bg"] = "#999999"
        ft = tkFont.Font(family='Calibri',size=14)
        Texte_Information_Label["font"] = ft
        Texte_Information_Label["fg"] = "#333333"
        Texte_Information_Label["justify"] = "center"
        Texte_Information_Label["text"] = "INFORMATION"
        Texte_Information_Label.place(x=940,y=90,width=339,height=41)

        Texte_IP_Label=tk.Label(root)
        Texte_IP_Label["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=15)
        Texte_IP_Label["font"] = ft
        Texte_IP_Label["fg"] = "#333333"
        Texte_IP_Label["justify"] = "center"
        Texte_IP_Label["text"] = f"IP : {ip}"
        Texte_IP_Label.place(x=940,y=130,width=339,height=30)

        Texte_DNS_Label=tk.Label(root)
        Texte_DNS_Label["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=15)
        Texte_DNS_Label["font"] = ft
        Texte_DNS_Label["fg"] = "#333333"
        Texte_DNS_Label["justify"] = "center"
        Texte_DNS_Label["text"] = f"DNS : {dns_resolv}"
        Texte_DNS_Label.place(x=940,y=160,width=339,height=30)

        Texte_Hostname_Label=tk.Label(root)
        Texte_Hostname_Label["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=15)
        Texte_Hostname_Label["font"] = ft
        Texte_Hostname_Label["fg"] = "#333333"
        Texte_Hostname_Label["justify"] = "center"
        Texte_Hostname_Label["text"] = f"Hostname : {host}"
        Texte_Hostname_Label.place(x=940,y=190,width=338,height=31)

        Texte_Semabox_ID_Label=tk.Label(root)
        Texte_Semabox_ID_Label["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=15)
        Texte_Semabox_ID_Label["font"] = ft
        Texte_Semabox_ID_Label["fg"] = "#333333"
        Texte_Semabox_ID_Label["justify"] = "center"
        Texte_Semabox_ID_Label["text"] = "SEMABOX UID :"
        Texte_Semabox_ID_Label.place(x=940,y=220,width=339,height=151)

        Texte_Return_ID_Label=tk.Label(root)
        Texte_Return_ID_Label["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=13)
        Texte_Return_ID_Label["font"] = ft
        Texte_Return_ID_Label["fg"] = "#333333"
        Texte_Return_ID_Label["justify"] = "left"
        Texte_Return_ID_Label["text"] = ID
        Texte_Return_ID_Label.place(x=950,y=310,width=329,height=53)

        Texte_Scan_De_Port_Label=tk.Label(root)
        Texte_Scan_De_Port_Label["bg"] = "#999999"
        ft = tkFont.Font(family='Calibri',size=18)
        Texte_Scan_De_Port_Label["font"] = ft
        Texte_Scan_De_Port_Label["fg"] = "#333333"
        Texte_Scan_De_Port_Label["justify"] = "center"
        Texte_Scan_De_Port_Label["text"] = "SCAN DE PORT"
        Texte_Scan_De_Port_Label.place(x=0,y=90,width=910,height=42)

        Texte_SPEEDTEST_Label=tk.Label(root)
        Texte_SPEEDTEST_Label["bg"] = "#999999"
        ft = tkFont.Font(family='Calibri',size=13)
        Texte_SPEEDTEST_Label["font"] = ft
        Texte_SPEEDTEST_Label["fg"] = "#333333"
        Texte_SPEEDTEST_Label["justify"] = "center"
        Texte_SPEEDTEST_Label["text"] = "SPEEDTEST"
        Texte_SPEEDTEST_Label.place(x=940,y=400,width=339,height=41)

        self.Resultat_Scan_Nmap_Label=tk.Label(root)
        self.Resultat_Scan_Nmap_Label["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=20)
        self.Resultat_Scan_Nmap_Label["font"] = ft
        self.Resultat_Scan_Nmap_Label["fg"] = "#333333"
        self.Resultat_Scan_Nmap_Label["justify"] = "center"
        self.Resultat_Scan_Nmap_Label["text"] = ""
        self.Resultat_Scan_Nmap_Label.place(x=0,y=130,width=722,height=587)

        Color_Background_Label=tk.Label(root)
        Color_Background_Label["bg"] = "#999999"
        ft = tkFont.Font(family='Calibri',size=10)
        Color_Background_Label["font"] = ft
        Color_Background_Label["fg"] = "#333333"
        Color_Background_Label["justify"] = "center"
        Color_Background_Label["text"] = ""
        Color_Background_Label.place(x=720,y=130,width=191,height=586)

        Button_scan_nmap=tk.Button(root)
        Button_scan_nmap["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=13)
        Button_scan_nmap["font"] = ft
        Button_scan_nmap["fg"] = "#ffffff"
        Button_scan_nmap["justify"] = "center"
        Button_scan_nmap["text"] = "SCAN"
        Button_scan_nmap.place(x=770,y=380,width=107,height=36)
        Button_scan_nmap["command"] = self.Button_scan_nmap_command

        self.Text_Label_Ping=tk.Label(root)
        self.Text_Label_Ping["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=11)
        self.Text_Label_Ping["font"] = ft
        self.Text_Label_Ping["fg"] = "#333333"
        self.Text_Label_Ping["justify"] = "center"
        self.Text_Label_Ping["text"] = "PING :" + "" + " ms"
        self.Text_Label_Ping.place(x=940,y=440,width=338,height=46)

        self.Text_Label_Montant=tk.Label(root)
        self.Text_Label_Montant["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=12)
        self.Text_Label_Montant["font"] = ft
        self.Text_Label_Montant["fg"] = "#333333"
        self.Text_Label_Montant["justify"] = "center"
        self.Text_Label_Montant["text"] = "Débit Montant : " + "" + " mb/s"
        self.Text_Label_Montant.place(x=940,y=480,width=339,height=48)

        self.Text_Label_Descendant=tk.Label(root)
        self.Text_Label_Descendant["bg"] = "#cdcdcd"
        ft = tkFont.Font(family='Calibri',size=12)
        self.Text_Label_Descendant["font"] = ft
        self.Text_Label_Descendant["fg"] = "#333333"
        self.Text_Label_Descendant["justify"] = "center"
        self.Text_Label_Descendant["text"] = "Débit Descendant : " + "" + " mb/s"
        self.Text_Label_Descendant.place(x=940,y=520,width=338,height=51)

        Color_Background2_Label=tk.Label(root)
        Color_Background2_Label["bg"] = "#999999"
        ft = tkFont.Font(family='Calibri',size=10)
        Color_Background2_Label["font"] = ft
        Color_Background2_Label["fg"] = "#333333"
        Color_Background2_Label["justify"] = "center"
        Color_Background2_Label["text"] = ""
        Color_Background2_Label.place(x=940,y=570,width=338,height=145)

        Button_speedtest=tk.Button(root)
        Button_speedtest["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=13)
        Button_speedtest["font"] = ft
        Button_speedtest["fg"] = "#ffffff"
        Button_speedtest["justify"] = "center"
        Button_speedtest["text"] = "SPEEDTEST"
        Button_speedtest.place(x=1050,y=610,width=125,height=40)
        Button_speedtest["command"] = self.Button_speedtest_command
        
        Button_clear_nmap=tk.Button(root)
        Button_clear_nmap["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=10)
        Button_clear_nmap["font"] = ft
        Button_clear_nmap["fg"] = "#ffffff"
        Button_clear_nmap["justify"] = "center"
        Button_clear_nmap["text"] = "CLEAR"
        Button_clear_nmap.place(x=770,y=440,width=110,height=37)
        Button_clear_nmap["command"] = self.Button_clear_nmap_command

        Button_speedtest_clear=tk.Button(root)
        Button_speedtest_clear["bg"] = "#393d49"
        ft = tkFont.Font(family='Calibri',size=10)
        Button_speedtest_clear["font"] = ft
        Button_speedtest_clear["fg"] = "#ffffff"
        Button_speedtest_clear["justify"] = "center"
        Button_speedtest_clear["text"] = "CLEAR"
        Button_speedtest_clear.place(x=1050,y=660,width=128,height=40)
        Button_speedtest_clear["command"] = self.Button_speedtest_clear_command

    def Button_scan_nmap_command(self):
        result_scan = scan_nmap()
        self.Resultat_Scan_Nmap_Label["text"] = result_scan


    def Button_speedtest_command(self):
        self.Text_Label_Ping["text"] = f"PING : {get_ping()} ms"
        self.Text_Label_Montant["text"] = f"Débit Montant : {get_download()} mb/s"
        self.Text_Label_Descendant["text"] = f"Débit Descendant : {get_upload_speed()}  mb/s"
        
    def Button_clear_nmap_command(self):
        self.Resultat_Scan_Nmap_Label["text"] = ""


    def Button_speedtest_clear_command(self):
        self.Text_Label_Ping["text"] = "PING :" + "" + " ms"
        self.Text_Label_Montant["text"] = "Débit Montant : " + "" + " mb/s"
        self.Text_Label_Descendant["text"] = "Débit Descendant : " + "" + " mb/s"
        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()






