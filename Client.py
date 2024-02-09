import socket
import sys

#Create socket object
try:
	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
	print("Couldn't create socket")
	
#Use host that user input
script,host = sys.argv

#Connect to a host address socket
socket.connect((host, 6969))

#Initial response
response="WAIT"


while True:
	
    #reciving WAIT from server
	while "WAIT" in response:
		response=socket.recv(4096).decode()
		print(response)
		
    #Take User command
	userInput= input("Game->")
	if(userInput==''):
		continue
	
    #Send user input to server
	socket.send(userInput.encode())
	
	# Collect response from server
	response=socket.recv(4096).decode()
	
    # Error
	if response=="400 ERR":
		print ("Invalid command Sent")
	
    #print : if command is valid
	else:
		print (response)
		
        #exit is command is Exit()
		if response=="DISC":
			sys.exit()

socket.close()

