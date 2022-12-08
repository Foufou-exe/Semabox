import socket
import platform

    
def _get_local_information():
    global ip_address, dns
    # Get the hostname of the current machine
    hostname = platform.node()

    # Get the IP address of the current machine
    ip_address = socket.gethostbyname(hostname)
    
    # Get the DNS of the current machine
    dns_resulte = socket.gethostbyaddr(ip_address)
    dns = dns_resulte[0]

_get_local_information()

