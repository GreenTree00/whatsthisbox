import platform
import psutil

class System:

    def __init__(self):
        self.architecture = platform.machine()       # e.g., 'AMD64', 'arm64'
        self.os = platform.system()                  # e.g., 'Windows', 'Linux'
        self.os_version = platform.version()         # Detailed OS version
        self.osv = platform.platform()               # Full OS descriptor
        self.hostname = platform.node()              # PC name

    def system_resources(self):
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_threads = psutil.cpu_count(logical=True)
        cpu_util = psutil.cpu_percent(interval=1)
        ram_util = psutil.virtual_memory().percent
        return f"""
System Resource Usage:
-----------------------
CPU Cores       : {cpu_cores}
CPU Threads     : {cpu_threads}
CPU Utilization : {cpu_util}%
RAM Utilization : {ram_util}%
"""