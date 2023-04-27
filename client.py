import socket
msg = input("mon message :")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# Connexion au serveur à partir des informations d'IP et de port contenues dans la classe
client.connect(('localhost', 3000))
client.send(msg.encode())
print (client.recv(255).decode())
