import socket


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
	inputMessage = input("Mesaj: ")
	if inputMessage == "quit":
		break
		
	message = bytes(inputMessage,"utf-8")
	clientSocket.sendto(message,('localhost',12000))