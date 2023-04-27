import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 3000))
            # Autorise le serveur à accepter jusqu'à 5 connexions
server.listen(5)

client,infosClient = server.accept()
msg = client.recv(255).decode()
print(msg)
msg = input ("msg : ")
client.send(msg.encode())
