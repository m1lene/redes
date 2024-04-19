from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 2222))
    serverSocket.listen()
    print("Aguardando conexões.. ")
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão estabelecida com", addr)
        connectionSocket.send("Bem-vindo ao atendimento de call center. Como posso ajudar?\nDigite 'Tchau' para encerrar a conversa.\n".encode())
        while True:
            message = connectionSocket.recv(2048).decode()
            print("Cliente:", message)
            if message.lower() == "tchau":
                print("Cliente encerrou a conversa.")
                break
            response = input("Atendente: ")
            connectionSocket.send(response.encode())
        connectionSocket.close()

if __name__ == '__main__':
    main()
