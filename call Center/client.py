from socket import *

def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 2222))
    while True:
        message = clientSocket.recv(2048).decode()
        if message.lower() == "tchau":
            print("Atendente encerrou a conversa.")
            break
        print("Atendente:", message)
        response = input("Cliente: ")
        clientSocket.send(response.encode())
    clientSocket.close()

if __name__ == '__main__':
    main()
