
gameover = 0
while(gameover == 0):
	import random as r
	comp = r.randint(0,2)
	print("Let's play Rock, Paper, Scissors!")
	player = input("Choose Rock, (0) Paper, (1) or Scissors (2) ")
	player = int(player)	
	if(comp == 0):
		print("I chose rock.")
	elif(comp == 1):
		print("I chose paper.")
	else:
		print("I chose scissors.")
	if(comp == player):
		print("It's a tie.")
		gameover = 0
	elif(comp == 2 and player == 0):
			print("You win!")
			gameover = 1
	elif(comp == 1 and player == 2):
			print("You win!")
			gameover = 1
	elif(comp == 0 and player == 1):
			print("You win!")
			gameover = 1
	elif(comp == 0 and player == 2):
		print("You lose.")
		gameover = 2
	elif(comp == 1 and player == 0):
		print("You lose.")
		gameover = 2
	else:
		print("You lose.")
		gameover = 2
