import socket
phone = socket.socket()
addr = (socket.gethostname(),8080)
phone.bind(addr)
phone.listen(17)
while True:
	try:
		conn, callid = phone.accept()
		msg = bytes.decode(conn.recv(1024))
		Conn.send(bytes.encode("r"))
		print("Call from {0}: {1}.".format(callid, msg))
	except KeyboardInterrupt:
		print("Leaving now, and never coming back!")
		phone.close()
		break
	finally:
		print("Leaving now, and never coming back!")
		phone.close()
		break
