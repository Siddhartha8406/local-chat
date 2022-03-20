from audioop import add
from concurrent.futures import thread
from email import message
from http import client, server
import msilib
import socket
from sqlite3 import connect
from threading import Thread, activeCount
from tokenize import cookie_re

client={} #TO STORE CLIENT USERNAME
address={} #TO STORE CLIENT IP ADDRESS

HEADER = 64     #HEADER SPECIFIES THE THE LENGHT OF THE MESSAGE FOLLOWED
PORT=5050   #PORT NO. OF THE SERVER
SERVER= socket.gethostbyname(socket.gethostname())  #Automatically gets the IP Address
FORMAT = 'utf-8'    #Setting the format of the encoding and decoding of the message
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #SPECIFIES THE CONNECTION TYPE
server.bind((SERVER, PORT)) #BINDS THE SERVER IP AND PORT

def handel_client(conn, addr):
    print(f"NEW STRING {addr} connected")

    connected = True
    while connected:
        msg_lenght = conn.recv(HEADER).decode(FORMAT)   #THE LENGHT OF THE MESSAGE FOLLOWED
        msg_lenght = int(msg_lenght)    #MAKES THE LENGHT INTO A INTERGER VALUE

        msg = conn.recv(msg_lenght).decode(FORMAT)
        print(f'[{addr}]: {msg}')

        if msg == DISCONNECT_MESSAGE:
            connected=False


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = Thread(target=handel_client, args=(conn, addr))    #CREATS A NEW THREAD FOR EACH USER
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {activeCount()-1}")    #PRINTS TO TOTAL CONNECTIONS, "-1" BECAUSE start() IS ALSO RUNNING ON A THREAD

if __name__ == '__main__':
    print("Server is starting")
    print(f"SERVER STATED ON {SERVER}:{PORT}")
    start