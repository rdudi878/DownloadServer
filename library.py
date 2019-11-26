# Download file
def download():
    

# Return current directory
def pwd(appType):
    if (appType=="client"):
        print("Current dir on client: ")
        print(os.getcwd)()
    if (appType=="server"):
        print("Current dir on server: ")
        currentDir = str(os.getcwd())
        c.send(currentDir)

# Change directory
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
            print(os.getcwd())
            if (appType=="server"):
                c.send(str(os.getcwd()))
        except OSError as e: # failsafe/catch for invalid path
            print(e)
            if (appType=="server"):
                c.send(e)

# Prints the contents of the current directory
def dir(appType):
    if (appType=="client"):
        dirContents = str(os.listdir(os.getcwd()))
        print(dirContents)
    if (appType=="server"):
        
