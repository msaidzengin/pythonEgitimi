import socket

receiverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiverSocket.bind(('',12000))
print("receiver is ready")

while 1:
	message,serverAddress = receiverSocket.recvfrom(2048)
	modifiedmessage = message.decode("utf-8")
	print(modifiedmessage)
