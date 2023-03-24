import socket
import threading

username=input("Enter you name : ")

client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("127.0.0.1",8000))

def recv():
    while True:
        try:
            msg=client.recv(2048).decode('utf-8')
            if msg:
                if msg=='###NICKNAME###':
                    client.send(username.lower().encode("utf-8"))
                else:
                    print(msg)
        except:
            pass

def write():
    while True:
        msg=f'{username} : {input("")}'
        client.send(msg.encode("utf-8"))

threading.Thread(target=recv).start()
threading.Thread(target=write).start()