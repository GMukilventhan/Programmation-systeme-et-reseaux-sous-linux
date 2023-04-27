#!/usr/bin/python

import threading , sys , socket


class Serveur():
	def _init_(self,IP,PORT):
		self.IP = IP
		self.PORT = PORT

		self.ID_client = 0
		self.infosocket = {"ID":[],"SOCKET":[]}
	def start(self):
		try:
			self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.server.bind((self.IP, self.PORT))
			self.server.listen(5)
		except:
			print("Impossible de démarrer le serveur")
			sys.exit()
		else:
			print("Serveur démarré")

	def accept(self):
		try:
			self.client,self.infosClient = self.server.accept()
		except:
			print("Impossible d'établir la connexion avec le client")
			sys.exit()
		else:
			self.ID_client = self.ID_client + 1
			self.infosocket["ID"].append(self.ID_client)
			self.infosocket["SOCKET"].append(self.client)

	def recv(self):
		try:
			rep = self.client.recv(255)
			return rep.decode()
		except:
			print("Impossible de recevoir le message")
			self.close()

	def send(self,msg):
		try:
			msg = msg.encode()
			self.client.send(msg)
		except : 
			print("Impossible d'envoyer un message")
			self.close()

	def Instruction(self,client, infosClient, server):   
		adresseIP = infosClient[0]
		port = str(infosClient[1])
		print("Démarrage des threads pour le client" + adresseIP + " : " +str(port))

		MESSAGE = self.recv().split(",")
		print (MESSAGE)


IP = "127.0.0.1"
PORT = 3402

SERVER = Serveur(IP,PORT)
SERVER.start()

threadsClients = []

while True:
	SERVER.accept()
	print("nombre de connection",threading.active_count())
	threadsClients.append(threading.Thread(None, SERVER.Instruction, None, (SERVER.client, SERVER.infosClient, SERVER.server), {}))
	threadsClients[-1].start()



#serveur.close()
