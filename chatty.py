import socket
import _thread
address = input("Enter address: ")
port = int(input("Enter port: ")

s = socket.socket()

s.connect(address, port)

while True:
	message = input("What is your message? ")
	s.sendall(message.encode("UTF-8"))



