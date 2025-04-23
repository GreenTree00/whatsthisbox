from argparse import ArgumentParser
from system import System
from network import Network

def main():
    system = System()
    network = Network()

    parser = ArgumentParser(description="Quickly view local IP and system resource usage")
    parser.add_argument("-net", help="Show basic network info", action="store_true")
    parser.add_argument("-sys", help="Show basic system resource info", action="store_true")
    args = parser.parse_args()

    if args.net:
        print(network.network())

    if args.sys:
        print(system.system_resources())