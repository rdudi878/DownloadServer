import sys
import socket
import os
import library as lib

if __name__ == '__main__':
	protocol = sys.argv[1] # Protocol: TCP or UDP
	host = '127.0.0.1'
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
				lib.pwd("client")
			elif(wordsSeparated[0]=="LCD"): # If first word is "LCD"
				print(lib.cd(wordsSeparated, "client"))
			elif(input=="LDIR"):
				lib.dir("client")
			else:
				s.sendall(input)
				message = s.recv(1024)
				print(message)
			# Needed for download:
				if(message=="READY"):
					print("Filename exists on server")
					dirContents = os.listdir(os.getcwd())
					match = False
					for i in dirContents: # scanning current dir for matching filename
						if(wordsSeparated[1]==i):
							match = True # found a matching filename on client current dir

					if(match==True):
						print("File {0} already exists. Overwrite? Y/N").format(wordsSeparated[1])
						overwrite = raw_input()
						if(overwrite=="y" or overwrite == "Y"):
							s.send("READY")
							file = open(wordsSeparated[1], 'wb')
							file_data = s.recv(1024)
							file.write(file_data)
							file.close()
							print("File has been received successfully")
						elif(overwrite=="n" or overwrite == "N"):
							s.send("STOP")
							reply = s.recv(1024)
							print(reply)
					elif(match==False):
						print("File {0} does not exist in current dir").format(wordsSeparated[1])
						s.send("READY")
						file = open(wordsSeparated[1], 'wb')
						file_data = s.recv(1024)
						file.write(file_data)
						file.close()
						print("File has been received successfully")
