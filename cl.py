import socket , time

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# Connexion au serveur à partir des informations d'IP et de port contenues dans la classe
client.connect(('127.0.0.1', 3402))
msg = "toto"
client.send(msg.encode())
time.sleep(7)
