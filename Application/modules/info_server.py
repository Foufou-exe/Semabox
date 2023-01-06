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

def api_info_server():
    hostname = get_hostname()
    ip = get_ip_address()
    dns = get_dns(ip)
    info_server = {
        'hostname': hostname,
        'ip': ip,
        'dns': dns
        
    }
    print(info_server)


if __name__ == "__main__":
    api_info_server()
