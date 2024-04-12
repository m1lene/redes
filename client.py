def main():
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(('127.0.0.1', 2222))
    
    while True:
        response = clientSocket.recv(2048).decode()
        if not response:
            print("Atendente encerrou a conexão.")
            break
        
        print("Atendente:", response)
        if response.lower() == "tchau":
            print("Atendente encerrou a conexão.")
            break
        
        message = input("Cliente: ")
        clientSocket.send(message.encode())
        if message.lower() == "tchau":
            print("Cliente encerrou a conexão.")
            break
    
    clientSocket.close()
