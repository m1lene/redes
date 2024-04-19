from socket import *

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serverSocket.bind(('', 2222))
    serverSocket.listen()
    print("Servidor aguardando conexoes...")

    while True:
        connectionSocket, addr = serverSocket.accept()
        try:
            message = connectionSocket.recv(1024).decode()

            # Obtendo a parte da URL que contém o nome do arquivo e a extensão
            file_requested = message.split()[1][1:]

            try:
                # Abrindo o arquivo solicitado e lendo seu conteúdo
                with open(file_requested, 'rb') as file:
                    content = file.read()

                # Enviando o cabeçalho da mensagem HTTP com o código de sucesso (200 OK)
                connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

                # Enviando o conteúdo do arquivo solicitado pelo cliente
                connectionSocket.send(content)

            except FileNotFoundError:
                # Enviando o cabeçalho da mensagem HTTP com o código de arquivo não encontrado (404 Not Found)
                connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())

        except Exception as e:
            print("Erro durante o processamento da requisição:", e)

        finally:
            connectionSocket.close()

    serverSocket.close()

if __name__ == '__main__':
    main()
