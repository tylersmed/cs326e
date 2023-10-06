###############################################################################
# server-python.py
# Name: Tyler Smedley
# EID: tws933
###############################################################################

import sys
import socket
import threading

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def handle_client(conn):
    
    while True:
        data = conn.recv(RECV_BUFFER_SIZE)
        if not data:
            break
        message = data.decode('utf-8')
        print(message, end='')

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'

    try:
        soc.bind((host, server_port))
    except socket.error as message:
        print('Bind failed. Error Code : '
          + str(message))
        sys.exit()

    while True:
        soc.listen(QUEUE_LENGTH)
        conn, addr = soc.accept()

        t = threading.Thread(target=handle_client, args=((conn,)))
        t.start()

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
