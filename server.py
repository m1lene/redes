from socket import * 

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 2222))
    serverSocket.listen()
    print("Aguardando conexões.. ")
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("conexao estabelecida", addr)
        message =connectionSocket.recv(2048)
        messageUpper = message.decode().upper()
        connectionSocket.send(messageUpper.encode())
    



if __name__ == '__main__':
    main()
