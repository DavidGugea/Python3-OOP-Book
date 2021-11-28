import socket
from ServerLogSocketDecorator import LogSocket

def respond(client):
    response = input("Enter a value: ")
    client.send(bytes(response, "utf-8"))
    client.close()


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((socket.gethostname(), 4000))
server.listen(1)

try:
    while True:
        client, addr = server.accept()
        respond(LogSocket(client))
finally:
    server.close()
