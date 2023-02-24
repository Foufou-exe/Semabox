import ifaddr
import ipaddress
def get_ip_vpn()->str:
    """
        Cette fonction permet de récupérer l'adresse IPv4 de l'interface "tun0" du système, qui est typiquement utilisée pour les connexions VPN.

        Retourne l'adresse IPv4 de l'interface "tun0" sous forme de chaîne de caractères.

        Si l'interface "tun0" n'est pas trouvée ou ne possède pas d'adresse IPv4, retourne None.

        Usage : 
        ip_vpn = get_ip_vpn()
        if ip_vpn:
            print("L'adresse IPv4 de l'interface 'tun0' est :", ip_vpn)
        else:
            print("L'interface 'tun0' n'est pas trouvée ou ne possède pas d'adresse IPv4.")

    """

    # Récupère les informations sur les interfaces réseau configurées sur le système
    # interfaces = ifaddr.get_adapters()
    # print(interfaces)
    # # Parcourt la liste des interfaces pour trouver celle qui s'appelle "tun0"
    # for interface in interfaces:
    #     if interface.nice_name == "Loopback Pseudo-Interface 1":
    #         # Récupère l'adresse IP de l'interface
    #         for ip in interface.ips:
    #             if ip.is_IPv4: 
    #                 print(ip.ip)
    #             break
    #         break
    # Nom de l'interface réseau dont vous souhaitez récupérer l'adresse IP
    # Nom de l'interface réseau dont vous souhaitez récupérer l'adresse IP
    interface_name = "OpenVPN TAP-Windows6"

    # Récupération des informations sur l'interface réseau
    adapter = None
    for ifa in ifaddr.get_adapters():
        if ifa.nice_name == interface_name:
            adapter = ifa
            break

    # Vérification que l'interface réseau a été trouvée
    if adapter is None:
        print(f"L'interface réseau {interface_name} n'a pas été trouvée.")
    else:
        # Récupération de l'adresse IP de l'interface réseau
        for ip in adapter.ips:
            if ip.is_IPv4:
                print(f"L'adresse IP de l'interface {interface_name} est : {ip.ip}")

get_ip_vpn()