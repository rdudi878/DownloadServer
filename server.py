import sys
import socket
import os
import library as lib
from socket import SHUT_RDWR

# Functions
# Download
def download(words):
	dirContents = os.listdir(os.getcwd())
	filename = words[1]
	for i in dirContents: # loop over every file in the current dir
		if(i==filename): # if there's a match
			c.send("READY") # send "READY" to the client
			listen = c.recv(16) # listen for a response
			if(listen=="READY"): # if "READY" is received
				print("Sending {0} to client").format(filename)
				f = open(filename, 'rb') # open the file to be copied
				f_data = f.read(1024) # read it and copy the data
				f.close() # close the file
				c.send(f_data) # send the data
				print("data has been sent")
			elif(listen=="STOP"): # otherwise, if "STOP", client wishes not to proceed
				c.send("OK, Will not overwrite file") # send confirmation to client
		else:
			c.send("File not found")

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

	if(words[0]=="BYE"):
		print("Received BYE message")
		s.shutdown(SHUT_RDWR)
		s.close()
	elif(words[0]=="PWD"):
		print("Received PWD command")
		currentDir = lib.pwd("server")
		c.send(currentDir)
	elif(words[0]=="DIR"):
		c.send(lib.dir("server"))
	elif(words[0]=="CD"):
		c.send(lib.cd(words, "server"))
	elif(words[0]=="DOWNLOAD"):
		print("Received DOWNLOAD command")
		download(words)
	else:
		print("Invalid command received")
		c.send("Invalid Command")
