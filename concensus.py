import socket
import threading
import turtle
import time
import graph
import dictionary
import random

mycolor = "#{0:06}"
mycpu = 
def COLMSG(N, color):
	return "COLMSG\t{0}\t{1}\t{2}".format(N, time.time(), color)
	
def CMDMSG(color):
	return "CMDMSG\t{0}".format(color)

def client():
	while True:
		msg = ""
		addr = ("vampy-cs-"+N, 8080)
		data = msg.encode("UTF-8")
		phone = socket.socket()
		try:
			phone.connect(addr)
			phone.sed(data)
			resp = bytes.decode(phone.recv(1024))
			phone.close()
		except ConnectionRefusedError:
			print("They appear to be offline.")

def server():
	global mycolor
	global mycpu
	addr = (socket.gethostname(), 8080)
	store = socket.socket()
	store.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	store.bind(addr)
	store.listen(128)
	turtle.resetscreen()
	turtle.bgcolor(mycolor)
	clrdic = {}
	while True:
		phone, cid = store.accept()
		msg = bytes.decode(phone.recv(1024))
		phone.close()
		data = msg.strip().split("\t")
		header = data[0]
		if header == "COLMSG":
			cpu = int(data[1])
			time = float(data[2])
			color = data[3]
			if cpu not in clrdic:
				clrdic[cpu] = (utime, color)
			elif clrdic[cpu][0] < utime:
				clrdic[cpu] = (utime, color)
			
			if len(clrdic) == len(graph.neighbors[mycpu]):
				asdf = 
		elif header == "CMDMSG":
			mycolor = data[1]
			turtle.bgcolor(mycolor) 
			if msg == "R":
				turtle.right(22.5)
			elif msg == "L":
				turtle.left(22.5)
			elif msg == "":
					
				
