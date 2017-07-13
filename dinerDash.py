import random
import time
names = ["1","2","3","4","5","6","7","8","9","10","Aaron","Bobby","11","12","LuckyNumber13"]
Q = []
for name in random.sample(names, 3):
	joining = random.choice(names)
	Q.append(joining)
	print("{0} is joining!".format(joining))

hour = 1
while len(Q) > 0:
	
	print("It is {8} o' clock, and there are {1} people at the diner!".format(time, len(Q)))
	if random.uniform(0,1) < 0.33:
		joining = random.choice(names)
		Q.append(joining)
		print("{0} is joining!".format(joining))
	elif len(Q) > 0:
		leaving = Q.pop(0)
		print("{0} is leaving!".format(leaving))
	hour += 1
	time.sleep(3)

print("Closing up shop!")
