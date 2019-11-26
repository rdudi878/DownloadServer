import sys
import socket
import os

# Functions

# Get current directory on the client
def lpwd():
	print("Current dir on client: ")
	print(os.getcwd())

# Change directory on the client
def lcd(words):
	if(len(words)<=1):
		print("Error. LCD requires 1 argument")
	if(len(words)>1):
		try:
			path = words[1] # path is the second word in the list
			os.chdir(path)
			print("Changed directory to:")
			print(os.getcwd())
		except OSError as e: # catches if the path is invalid
			print(e)
			
# Directory content listing on client
def ldir():
	dirContents = str(os.listdir(os.getcwd()))
	print(dirContents)
	


if __name__ == '__main__':
	protocol = sys.argv[1] # Protocol: TCP or UDP
	host = '172.31.20.35'
# 172.31.20.35
	if (protocol=='tcp'):
		# AF_INET indicates IPV4. SOCK_STREAM indicates that this is a TCP socket
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		try:
			print(host)
			# connect accepts 1 arg, a tuple containing hostname, and a port number
			s.connect((host, 7778))
			data = s.recv(1024) # 1024 is an arbitrary number of bytes to receieve
			print(data)
		except:
			print("Connection failed. Invalid hostname.")
			exit()
		while True:
			input = raw_input()
			wordsSeparated = input.split()
			if(input=="LPWD"):
				lpwd()
			elif(wordsSeparated[0]=="LCD"): # If first word is "LCD"
				lcd(wordsSeparated) # pass lcd() a list containing the path
			elif(input=="LDIR"):
				ldir()
			else:
				s.sendall(input)
				message = s.recv(1024)
				print(message)
	