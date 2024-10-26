import threading
import socket

def main():
    #AF_INET = IPV4 e SOCK_STREAM = TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect(('localhost', 1533))
    except:
        return print("Não foi possível se conectar ao servidor.")
    
    username = input("Digite aqui o seu username:\n")
    print("Conectado")

    thread1 = threading.Thread(target=receiveMessage, args=[client])
    thread2 = threading.Thread(target=sendMessage, args=[client, username])

    thread1.start()
    thread2.start()

def receiveMessage(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg)
        except:
            print("\nNão foi possível permanecer conectado no servidor!")
            print("Pressione <Enter> para continuar...")
            client.close()
            break

def sendMessage(client, username):
    while True:
        try:
            msg = input("\n")
            client.send(f'<{username}> {msg}'.encode('utf-8'))
        except:
            return



main()