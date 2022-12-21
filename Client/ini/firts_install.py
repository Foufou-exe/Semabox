import os
from modules.info_server import get_ip_address as ip, get_hostname as hostname, get_dns as dns

sambox = {"IP": ip, "HOSTNAME": hostname, "DNS": dns}
print(sambox)
