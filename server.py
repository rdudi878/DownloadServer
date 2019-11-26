import sys
import socket
import os
from socket import SHUT_RDWR


# Functions

# Change Directory
def cd(words):
	print("Received CD command")
	if(len(words)<=1):
		print("Error. CD requires 1 argument")
	if(len(words)>1):
		try:
			path = words[1] # path is the second word in the list
			os.chdir(path)
			print("Changed directory to:")
			print(os.getcwd())
			c.send(str(os.getcwd()))
		except OSError as e: # catches if the path is invalid
			print(e)
			c.send(e)
	

try:
	s = socket.socket()
	print("Socket successfully created")
	print(socket.gethostbyname(socket.gethostname()))
	print(socket.gethostname())
except socket.error as err:
	print("Socket creation failed with error %s" %(err))

port = 7778
try:
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind(('', port))
	print("Socket binded to port %s" %(port))
except socket.error as err:
	print("Error binding socket: %s" %(err))

hostname = socket.gethostname()
print(socket.gethostbyname(hostname))

s.listen(5)
print("Socket is listening")
c, addr = s.accept()
print("Got connection from", addr)
print("Sending HELLO message to", addr)
c.send("HELLO")

while True:
	data = c.recv(16)
	words = data.split()

	if(data=="BYE"):
		print("Received BYE message")
		s.shutdown(SHUT_RDWR)
		s.close()
	elif(data=="PWD"):
		print("Received PWD command")
		currentDir = str(os.getcwd())
		c.send(currentDir)
	elif(data=="DIR"):
		print("Received DIR command")
		dirContents = str(os.listdir(os.getcwd()))
		c.send(dirContents)
	elif(words[0]=="CD"):
		cd(words)
	elif(data=="DOWNLOAD"):
		print("Received DOWNLOAD command")
	else:
		print("Invalid command received")
		c.send("Invalid Command")