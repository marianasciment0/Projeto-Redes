import threading
import socket

clients = []

def main():
    
    #AF_INET = IPV4 e SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 1533))
        server.listen(5) #Se não colocarmos nada, ele aceitará infinitas conexões
        #Porém se colocamos um inteiro como parâmetro, ele aceitará o número de conexões que indicarmos
        print("Servidor iniciado!")
    except:
        print("Não foi possível iniciar o servidor.") 
        return

    while True:
        client, addr = server.accept()
        clients.append(client)
        print(f"Conexão estabelecida com {addr}")

        #Aqui ele cria uma thread para cada client que se conectar na rede
        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break

def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(client)

def deleteClient(client):
    clients.remove(client)
    print(f"{client} desconectado")

main()