from argparse import ArgumentParser
from .my_system import System
from .network import Network

def main():
    my_system = System()
    network = Network()

    parser = ArgumentParser(description="Quickly view local IP and system resource usage")
    parser.add_argument("-net", help="Show basic network info", action="store_true")
    parser.add_argument("-sys", help="Show basic system resource info", action="store_true")
    args = parser.parse_args()

    if args.net:
        print(network.network())

    if args.sys:
        print(my_system.system_resources())

if __name__ == "__main__":
    main()
