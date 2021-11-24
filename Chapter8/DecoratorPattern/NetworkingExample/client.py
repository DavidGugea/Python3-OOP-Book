import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((socket.gethostname(), 4000))
print("Received: {0}".format(client.recv(1024)))
client.close()
