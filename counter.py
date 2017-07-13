import _thread
import time
import threading
counter = 0
lock = threading.Lock()
def counter_work(name, delay):
	global counter
	global lock
	while counter < 100000:
		time.sleep(delay)
		lock.acquire()
		counter += 1
		print(counter, name)
		lock.release()
	
for i in range(10000):
	_thread.start_new_thread(counter_work, ("Thread "+str(i+1), 1))
	time.sleep(0.0001)

while counter < 100000:
	pass
