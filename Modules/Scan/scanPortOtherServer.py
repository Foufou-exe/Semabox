import nmap  # Pour scanner


# Fonctions
def scan_port_other_machine(ip_args) -> str:

    """
    Description:
        Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne une chaîne de caractères contenant les informations sur les ports ouverts.
    """
    try:
        # Création d'un objet nmap.PortScanner()
        nm = nmap.PortScanner()

        # Adresse IP de l'hôte à scanner
        host = ip_args
        # On scanne l'hôte en utilisant l'option -sS (SYN scan)
        nm.scan(host, arguments="-sS")

        # On construit la chaîne de caractères à partir des informations sur les ports ouverts
        return "".join(
            f"\nPort {port}/tcp | OPEN | service : {nm[host]['tcp'][port]['name']}"
            for port in nm[host]["tcp"]
            if nm[host]["tcp"][port]["state"] == "open"
        )

    except KeyError as e:
        if e.args[0] == "tcp":
            return "Aucun Port ouvert"


def api_scan_port_other_machine(ip_args) -> dict:

    """
    Description:
        Cette fonction scanne les ports ouverts sur l'hôte local en utilisant l'outil nmap et retourne un dictionnaire
        contenant les informations sur les ports ouverts.
    """
    try:
        # Création d'un objet nmap.PortScanner()
        nm = nmap.PortScanner()

        # Adresse IP de l'hôte à scanner
        host = str(ip_args)

        # On scanne l'hôte en utilisant l'option -sS (SYN scan)
        nm.scan(host, arguments="-sS")

        scan_results = {
            port: {"port": port, "state": data["state"], "service": data["name"]}
            for port, data in nm[host]["tcp"].items()
            if data["state"] == "open"
        }

        return scan_results

    except KeyError as e:
        if e.args[0] == "tcp":
            print({"message": "Aucun Port ouvert"})


if __name__ == "__main__":
    api_scan_port_other_machine()
