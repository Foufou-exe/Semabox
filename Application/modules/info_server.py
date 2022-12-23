import socket
import platform


def get_hostname():
    # Get the hostname of the current machine
    return platform.node()

def get_ip_address():
    # Get the ip address of the current machine
    return socket.gethostbyname(socket.gethostname())


def get_dns(ip):    
    # Get the DNS of the current machine
    dns_resulte = socket.gethostbyaddr(ip)
    return dns_resulte[0]


if __name__ == "__main__":
    print(get_hostname())
    print(get_ip_address())
    print(get_dns(get_ip_address()))