import sys
import socket
import os
import library as lib
from socket import SHUT_RDWR


# Return current directory - LOOKS GOOD
def pwd(appType):
    if (appType=="client"):
        print("Current dir on client: ")
        print(os.getcwd)()
    if (appType=="server"):
        print("Current dir on server: ")
        currentDir = str(os.getcwd())
        return currentDir

# Change directory - LOOKS GOOD
def cd(words, appType):
    if (appType=="server"):
        print("Received CD command")
    if (len(words)<=1):
        print("Error: CD requires 1 argument")
    if (len(words)>1):
        try:
            path = words[1] # path to second word in list
            os.chdir(path)
            print("Changed directory to:")
            success = str(os.getcwd())
            return success
        except OSError as e: # failsafe/catch for invalid path
            return str(e)

# Prints the contents of the current directory - LOOKS GOOD
def dir(appType):
    dirContents = os.listdir(os.getcwd())
    ppDirContents = ', '.join(dirContents)
    if (appType=="client"):
      print(ppDirContents)
    elif (appType=="server"):
      print("Received DIR command")
      return ppDirContents

