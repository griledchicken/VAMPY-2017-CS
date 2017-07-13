import socket

while True:
	N     = input("Who ya gonna call? ")
	msg   = input("Whatcha gonna say? ")
	data  = msg.encode("UTF-8")
	addr  = ("vampy-cs-"+N, 4242)
	phone = socket.socket()
	phone.connect(addr)
	phone.send(data)
	resp  = bytes.decode(phone.recv(1024))
	if resp != "r":
		print("MESSAGE FAILED")
	


