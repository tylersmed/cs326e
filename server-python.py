###############################################################################
# server-python.py
# Name: Tyler Smedley
# EID: tws933
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'

    try:
        soc.bind((host, server_port))
    except socket.error as message:
        print('Bind failed. Error Code : '
          + str(message[0]) + ' Message '
          + message[1])
        sys.exit()

    soc.listen(QUEUE_LENGTH)
    conn, addr = soc.accept()

    while True:
        data = conn.recv(RECV_BUFFER_SIZE)
        if not data:
            break
        print(data)


def main():
    """Parse command-line argument and call server function """
    while True:
        if len(sys.argv) != 2:
            sys.exit("Usage: python server-python.py [Server Port]")
        server_port = int(sys.argv[1])
        server(server_port)

if __name__ == "__main__":
    main()
