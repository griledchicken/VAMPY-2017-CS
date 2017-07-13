import random as r
dice = input("What kind of dice would you like to roll? Choose between d4, d6, d8, d10, d12, d20, d100, or dcustomNumber(just type a number) ")
if dice in["D4", "d4"]:
	dice4 = r.randint(1,4)
	print(str(dice4))
elif dice in["D6", "d6"]:
	dice6 = r.randint(1,6)
	print(str(dice6))
elif dice in["D8", "d8"]:
	dice8 = r.randint(1,8)
	print(str(dice8))
elif dice in["D10", "d10"]:
	dice10 = r.randint(1,10)
	print(str(dice10))
elif dice in["D12", "d12"]:
	dice12 = r.randint(1,12)
	print(str(dice12))
elif dice in["D20", "d20"]:
	dice20 = r.randint(1,20)
	print(str(dice20))
elif dice in ["d100","D100"]:
	dice100 = r.randint(1,100)
	print(str(dice100))
else:
	diceW = int(dice)
	diceX = r.randint(1,diceW)
	print(str(diceX))
	
