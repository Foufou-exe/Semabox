#!/usr/bin/env python3.11.1

# Importation des librairies nécessaires
import requests
import time
import icmplib
import os
import asyncio
import aiohttp


class Speedtest:

    # Définition des variables
    TEST_FILE_URL = (
        "http://ipv4.download.thinkbroadband.com/50MB.zip"  # Fichier de 50 MB
    )
    UPLOAD_URL = "https://www.googleapis.com/upload/drive/v3/files?uploadType=media"  # URL de téléchargement
    FILE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "TESTMB.zip"
    )  # Chemin d'accès au fichier de test à télécharger
    HOST = "google.com"  # Hôte à ping*

    @staticmethod
    async def get_download_speed(url=TEST_FILE_URL) -> str:
        download_start_time = time.time()  # Début du téléchargement
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:  # Téléchargement du fichier
                download_end_time = time.time()  # Fin du téléchargement
                elapsed_time = (
                    download_end_time - download_start_time
                )  # Durée du téléchargement
                download_speed = (
                    len(await response.read()) / elapsed_time
                )  # Vitesse de téléchargement
                return "{0:.2f}".format(
                    download_speed / 1000000 * 8
                )  # Retourne la vitesse de téléchargement en mégabits par seconde

    @staticmethod
    async def get_upload_speed(file_path=FILE_PATH, url=UPLOAD_URL) -> str:
        with open(file_path, "rb") as file:  # Ouverture du fichier
            upload_start_time = time.time()  # Début timer de l'envoi
            async with aiohttp.ClientSession() as session:
                files = {"file": file}  # Fichier à envoyer
                async with session.post(
                    url, data=files
                ) as response:  # Envoi du fichier
                    upload_end_time = time.time()  # Fin timer de l'envoi
                    upload_speed = len(await response.read()) / (
                        upload_end_time - upload_start_time
                    )  # Vitesse d'envoi
                    return "{0:.2f}".format(
                        upload_speed
                    )  # Retourne la vitesse d'envoi en mégabits par seconde

    @staticmethod
    def get_ping(host=HOST) -> int:
        while True:  # Boucle infinie
            icmp = icmplib.ping(host, count=1)  # Envoie une requête ICMP
            return int(icmp.avg_rtt)  # Retourne la durée du ping en millisecondes

    @staticmethod
    def ping(host=HOST) -> int:
        icmp = icmplib.ping(host, count=1)  # Envoie une requête ICMP
        return int(icmp.avg_rtt)  # Retourne la durée du ping en millisecondes


async def api_speedtest() -> dict:
    speedtest = Speedtest()  # Création de l'objet Speedtest

    # Appeler les fonctions asynchrones en parallèle avec `asyncio.gather`
    download_speed_task = asyncio.create_task(speedtest.get_download_speed())
    upload_speed_task = asyncio.create_task(speedtest.get_upload_speed())

    download_speed = await download_speed_task
    upload_speed = await upload_speed_task
    ping = speedtest.ping()  # Ping
    result = {
        "download_speed": download_speed,
        "upload_speed": upload_speed,
        "ping": ping,
    }  # Dictionnaire contenant les vitesses de téléchargement, d'envoi et de ping
    return result


if __name__ == "__main__":
    print(asyncio.run(api_speedtest()))
