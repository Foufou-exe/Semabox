import sys
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# def get_webdriver(browser):
#     if browser.lower() == "chrome":
#         options = webdriver.ChromeOptions()
#         options.add_argument("--headless")
#         return webdriver.Chrome(options=options)
#     elif browser.lower() == "firefox":
#         options = webdriver.FirefoxOptions()
#         options.add_argument("--headless")
#         return webdriver.Firefox(options=options)
#     elif browser.lower() == "edge":
#         options = webdriver.EdgeOptions()
#         options.add_argument("--headless")
#         return webdriver.Edge(options=options)
#     else:
#         raise ValueError("Browser non pris en charge")

# if len(sys.argv) > 1:
#     browser = sys.argv[1]
# else:
#     browser = "chrome"

# driver = get_webdriver(browser)
# driver.get("https://www.speedtest.net/")
# time.sleep(3)
# rgpd_button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
# rgpd_button.click()
# go_button = driver.find_element(By.CSS_SELECTOR, '.start-button a')
# go_button.click()

# time.sleep(48)
# # Attendre que les résultats du test de vitesse apparaissent
# wait = WebDriverWait(driver, 5)
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data-large.number.result-data-value.download-speed')))
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data-large.number.result-data-value.upload-speed')))
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data-value.ping-speed')))
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'js-data-sponsor')))
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data.js-sponsor-name')))
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-data.js-data-ip')))
# wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-label.js-data-isp')))

# # Extraire les résultats du test de vitesse
# download_speed = driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.download-speed').text
# upload_speed = driver.find_element(By.CLASS_NAME, 'result-data-large.number.result-data-value.upload-speed').text
# ping_speed = driver.find_element(By.CLASS_NAME, 'result-data-value.ping-speed').text

# Nom_du_fournisseur = driver.find_element(By.CLASS_NAME, 'js-data-sponsor').text
# Nom_Serveur = driver.find_element(By.CLASS_NAME, 'result-data.js-sponsor-name').text

# IP_PUBLIC = driver.find_element(By.CLASS_NAME, 'result-data.js-data-ip').text
# Nom_de_votre_fournisseur = driver.find_element(By.CLASS_NAME, 'result-label.js-data-isp').text

# # Imprimer les résultats du test de vitesse
# print('Débit descendant :', download_speed)
# print('Débit montant :', upload_speed)
# print('Ping :', ping_speed)

# print('Nom du fournisseur :', Nom_du_fournisseur)
# print('Nom de votre ISP :', Nom_Serveur)

# print('IP PUBLIC :', IP_PUBLIC)
# print('Nom du fournisseur :', Nom_de_votre_fournisseur)

# # Ferme le navigateur Web
# driver.quit()


class Speedtest:
    def ipinfo(self):
        response = requests.get("http://ipinfo.io/json")
        data = response.json()
        ip_public = data["ip"]
        city = data["city"]
        region = data["region"]
        country = data["country"]
        operator = data["org"]

        driver = self._extracted_from_speedtest_10()
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located((By.ID, "onetrust-accept-btn-handler"))
        )
        rgpd_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        rgpd_button.click()

        Nom_du_fournisseur = driver.find_element(By.CLASS_NAME, "hostUrl").text
        Nom_Serveur = driver.find_element(By.CLASS_NAME, "name").text

        driver.quit()

        return [
            ip_public,
            city,
            region,
            country,
            operator,
            Nom_du_fournisseur,
            Nom_Serveur,
        ]

    def speedtest(self):
        driver = self._extracted_from_speedtest_10()
        rgpd_button = driver.find_element(By.ID, "onetrust-accept-btn-handler")
        rgpd_button.click()
        go_button = driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(47)
        # Attendre que les résultats du test de vitesse apparaissent
        wait = WebDriverWait(driver, 5)
        wait.until(
            EC.visibility_of_element_located(
                (
                    By.CLASS_NAME,
                    "result-data-large.number.result-data-value.download-speed",
                )
            )
        )
        wait.until(
            EC.visibility_of_element_located(
                (
                    By.CLASS_NAME,
                    "result-data-large.number.result-data-value.upload-speed",
                )
            )
        )
        wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "result-data-value.ping-speed")
            )
        )

        # Extraire les résultats du test de vitesse
        download_speed = driver.find_element(
            By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed"
        ).text
        upload_speed = driver.find_element(
            By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed"
        ).text
        ping_speed = driver.find_element(
            By.CLASS_NAME, "result-data-value.ping-speed"
        ).text
        # Ferme le navigateur Web
        driver.quit()

        return [
            download_speed,
            upload_speed,
            ping_speed,
        ]

    # TODO Rename this here and in `ipinfo` and `speedtest`
    def _extracted_from_speedtest_10(self):
        browser = sys.argv[1] if len(sys.argv) > 1 else "chrome"
        result = self.get_webdriver(browser)
        result.get("https://www.speedtest.net/")
        time.sleep(5)
        return result

    def get_webdriver(self, browser):
        if browser.lower() == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument(
                "--log-level=3"
            )  # Désactive les messages de la console
            options.add_experimental_option(
                "excludeSwitches", ["enable-logging"]
            )  # Désactive les messages d'enregistrement
            return webdriver.Chrome(options=options)
        elif browser.lower() == "firefox":
            options = webdriver.FirefoxOptions()
            options.add_argument("--headless")
            options.log.level = "fatal"  # N'affiche que les messages d'erreur fatale
            return webdriver.Firefox(options=options)
        elif browser.lower() == "edge":
            options = webdriver.EdgeOptions()
            options.add_argument("--headless")
            options.add_argument(
                "--log-level=3"
            )  # Désactive les messages de la console
            return webdriver.Edge(options=options)
        else:
            raise ValueError("Browser non pris en charge")


if __name__ == "__main__":
    speedtest = Speedtest()
    print(speedtest.ipinfo())
