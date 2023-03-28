# from tkinter import ttk
# from ttkbootstrap import *
# from ttkwidgets import *
# import tkinter as tk
# import asyncio

# import sys

# sys.path.append('Modules')
# from Information.info import InfoServer
# from Scan.scanPort import ScanPort
# from Scan.scanAllServer import ScanAllServer
# from Scan.scanPortOtherServer import scan_port_other_machine
# from Speedtest.speedtest import Speedtest
# from Serveur.update import *


# def update_meter(download_speed, upload_speed):
#     download_meter.set_amount(download_speed)
#     upload_meter.set_amount(upload_speed)
#     window.update_idletasks()

# async def test_speed():

#     # Appeler les fonctions asynchrones en parallèle avec `asyncio.gather`
#     download_speed_task = asyncio.create_task(Speedtest.get_download_speed())
#     upload_speed_task = asyncio.create_task(Speedtest.get_upload_speed())

#     download_speed, upload_speed = await asyncio.gather(download_speed_task, upload_speed_task)
#     # download_label.config(text=f"Download: {str(download_speed)} Mbps")
#     # upload_label.config(text=f"Upload: {str(upload_speed)} Mbps")

#     update_meter(download_meter, download_speed)
#     update_meter(upload_meter, upload_speed)


# # Créer une fenêtre tkinter
# window = tk.Tk()
# window.title("SpeedTest")

# # Appliquer le thème ttkbootstrap
# style = Style()
# style.theme_use("superhero")

# test_button = ttk.Button(window, text="SpeedTest", command=lambda: asyncio.run(test_speed()))
# test_button.pack(pady=20)

# download_meter = Meter(
#     master=window,
#     metersize=250,
#     amountused=0,
#     textfont=("Helvetica", 20, "bold"),
#     textright="Mbps",
#     subtext="Débit Montant",
#     subtextfont=("Helvetica", 10, "bold"),

# )
# download_meter.pack(pady=(0, 10))
# download_label = ttk.Label(window, text="Download")
# download_label.pack()

# upload_meter = Meter(
#     master=window,
#     metersize=250,
#     amountused=0,
#     textfont=("Helvetica", 20, "bold"),
#     textright="Mbps",
#     subtext="Débit Descendant",
#     subtextfont=("Helvetica", 10, "bold"),
# )
# upload_meter.pack(pady=(20, 10))
# upload_label = ttk.Label(window, text="Upload")
# upload_label.pack()

# window.mainloop()

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from yspeed import Yspeed

my_w = ttk.Window()
my_w.geometry("680x300")  # width and height

m1 = ttk.Meter(
    my_w,
    amounttotal=1,
    amountused=0,
    meterthickness=20,
    bootstyle=INFO,
    metersize=200,
    stripethickness=6,
    subtext="Download",
    textright="Mbps",
)
m1.grid(row=1, column=1, padx=5, pady=10)
m2 = ttk.Meter(
    my_w,
    amounttotal=1,
    amountused=0,
    meterthickness=20,
    bootstyle=INFO,
    metersize=200,
    stripethickness=6,
    subtext="Upload",
    textright="Mbps",
)
m2.grid(row=1, column=2, padx=5, pady=10)

m3 = ttk.Meter(
    my_w,
    amounttotal=1,
    amountused=0,
    meterthickness=20,
    bootstyle=INFO,
    metersize=200,
    stripethickness=6,
    subtext="Ping",
    textright="Ms",
)
m3.grid(row=1, column=3, padx=5, pady=10)


def my_second():
    y = Yspeed()
    result = y.get_speedtest()
    m1["amountused"] = "{download}".format(**result)  #  update meter value
    m1["bootstyle"] = "success"
    m2["amountused"] = "{upload}".format(**result)  #  update meter value
    m2["bootstyle"] = "success"
    m3["amountused"] = "{ping}".format(**result)  #  update meter value
    m3["bootstyle"] = "success"


b1 = ttk.Button(my_w, text="Start", command=my_second)
b1.grid(row=2, column=1)
my_w.mainloop()
