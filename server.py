import socket
import threading

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address="127.0.0.1"
port=8000
server.bind((ip_address,port))

server.listen()

print("[START] server has started")


def client_thread(conn,username):
    conn.send("Welcome to the server".encode("utf-8"))
    while True:
        try:
            msg=conn.recv(2048).decode("utf-8")
            if msg:
                print(msg)
        except:
            remove_conn(conn)
            remove_nickname(username)
    
def remove_conn(conn):
    if conn in clients:
        clients.remove(conn)

def remove_nickname(username):
    if username in nicknames:
        nicknames.remove(username)


clients=[]
nicknames=[]

while True:
    conn,addr=server.accept()
    conn.send("###NICKNAME###".encode("utf-8"))

    username=conn.recv(2048).decode("utf-8")

    clients.append(conn)
    nicknames.append(username)

    print(f'{username} just connected to the server')

    threading.Thread(target=client_thread,args=(conn,username)).start()