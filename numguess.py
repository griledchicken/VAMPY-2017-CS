lower = 0
upper = 0
guess = 1
ans = ""
while ans != "equal":
	ans = input("Is "+str(guess)+" equal to your number, or should I go more or less? (equal/less/more): ")
	if ans == "more":
		if upper == 0:
			guess *= 2
		else:
			lower = guess
			guess = int((lower + upper)/2)
	elif ans == "less":
		if upper == 0:
			lower = int(guess / 2)

		upper = guess
		guess = int((lower + upper)/2)

print("Woohoo, I found your number!!! It was "+str(guess)+".")
