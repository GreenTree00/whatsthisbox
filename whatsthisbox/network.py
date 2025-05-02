import platform
import socket

class Network:

    def __init__(self):
        self.hostname = platform.node()
        try:
            self.ip = socket.gethostbyname(self.hostname)
        except socket.gaierror:
            self.ip = "Unable to fetch IP address"

    def network(self):
        return f"""
Network Information:
---------------------
Hostname    : {self.hostname}
IP Address  : {self.ip}
"""
