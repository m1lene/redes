from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('127.0.0.1', 2222))
    serverSocket.listen()
    print("Aguardando conexões.. ")
    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Conexão estabelecida com", addr)
        connectionSocket.send("Bem-vindo ao atendimento de call center! Como posso ajudá-lo?".encode())
        
        while True:
            message = connectionSocket.recv(2048).decode()
            print("Cliente:", message)
            if message.lower() == "tchau":
                print("Cliente encerrou a conexão.")
                break
            
            response = input("Atendente: ")
            connectionSocket.send(response.encode())
            if response.lower() == "tchau":
                print("Atendente encerrou a conexão.")
                break

        connectionSocket.close()

if __name__ == '__main__':
    main()
