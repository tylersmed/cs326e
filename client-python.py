###############################################################################
# client-python.py
# Name: Tyler Smedley
# EID: tws933
###############################################################################

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
        soc.connect((server_ip, server_port))
        buf = sys.stdin.buffer.read(2048)
        while buf:
            soc.sendall(buf)
            buf = sys.stdin.buffer.read(2048)

    soc.close()

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
