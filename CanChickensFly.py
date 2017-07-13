answer = input("Can Chickens Fly? YES/NO: ")
if answer == "YES":
	answer = input("Can they fly well? YES/NO: ")
	if answer == "YES":
		answer = input("Have you ever seen a Chicken? YES/NO: ")
		if answer == "YES":
			print("You're lying to me")
		else:
			print("Go take a look at one")
	else:
		answer = input("Have you ever seen a Chicken? YES/NO: ")
		if answer == "YES":
			print("I figured")
		else:
			print("You're smart")
else:
	answer = input("Can they jump? YES/NO: ")
	if answer == "YES":
		answer = input("Have you ever seen a Chicken? YES/NO: ")
		if answer == "YES":
			print("I figured")
		else:
			print("You're smart")
	else:
		answer = input("Have you ever seen a Chicken? YES/NO: ")
		if answer == "YES":
			print("You're lying to me")
		else:
			print("Go take a look at one")
