from socket import * 

def main():
       clientSocket = socket(AF_INET, SOCK_STREAM)
       clientSocket.connect(('127.0.0.1)', 2222))
       message = input("mensagem:")
       clientSocket.send(message.encode())
       response, addr = clientSocket.recv(2048)
       print(response.decode())
       clientSocket.close()

if __name__ == '__main__':
    main()
