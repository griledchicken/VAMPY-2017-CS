appPrice = 0
mainPrice = 0
desPrice = 0
sutotPrice = 0
taxprice = 0
tipPrice = 0
totPrice = 0
f = open("reciept.txt","w")
appBool = input("Did you order an appetizer? ")
if appBool in ["YES", "Yes", "yes"]:
	appType = input("What did you order? Was it soup or salad? ")
	if appType in ["SOUP", "Soup", "soup"]:
		appPrice = 7
	elif appType in ["SALAD", "Salad", "salad"]:
		appPrice = 5
mainBool = input("Did you order a main course? ")
if mainBool in ["YES", "Yes", "yes"]:
	mainType = input("What did you order? Was it steak, chicken, or pasta? ")
	if mainType in ["STEAK", "Steak", "steak"]:
		mainPrice = 14
	elif mainType in ["CHICKEN", "Chicken", "chicken"]:
		mainPrice = 12
	elif mainType in ["PASTA", "Pasta", "pasta"]:
		mainPrice = 11
desBool = input("Did you order dessert? ")
if desBool in ["YES", "Yes", "yes"]:
	desType = input("What did you order? Was it cake or ice cream? ")
	if desType in ["Cake", "Cake", "cake"]:
		desPrice = 8
	elif desType in ["ICE CREAM", "Ice Cream", "Ice cream", "ice cream"]:
		desPrice = 6

tipBool = input("Would you like to leave a tip? ")

print("Appetizer: $"+str(appPrice)+".00")
print("Main Course: $"+str(mainPrice)+".00")
print("Dessert: $"+str(desPrice)+".00")
sutotPrice = appPrice + mainPrice + desPrice
print("Subtotal: $"+str(sutotPrice)+".00")
taxPrice = float(sutotPrice) *(0.06)
if taxPrice % 1 == 0:
	print("Tax: $"+str(taxPrice)+".00")
elif taxprice % 0.1 == 0:
	print("Tax: $"+str(taxPrice)+"0")
else:
	taxPrice = round(1/2, 2)taxPrice	
	print("Tax: $"+str(taxPrice))
if tipBool in ["YES", "Yes", "yes"]:
	tipPrice = sutotPrice*(0.2)

if tipPrice % 1 == 0:
	print("Tip: $"+str(tipPrice)+".00")
elif tipPrice % .1 == 0:
	print("Tip: $"+str(tipPrice)+"0")
else:
	tipPrice = round(1/2, 2)tipPrice
totPrice = sutotPrice + taxPrice + tipPrice
if totPrice % 1 == 0:
	print("Tip: $"+str(totPrice)+".00")
elif totPrice % 0.1 == 0:
	print("Tip: $"+str(totPrice)+"0")

f.write("Appetizer: $"+str(appPrice)+".00"+"\n")
f.write("Main Course: $"+str(mainPrice)+".00"+"\n")
f.write("Dessert: $"+str(desPrice)+".00"+"\n")
f.write("Subtotal: $"+str(sutotPrice)+".00"+"\n===================\n")
f.write("Tax: $"+str(taxPrice)+"\n")
f.write("Tip: $"+str(tipPrice)+"\n")
f.write("Total: $"+str(totPrice)+"\n")


#f = open("Grades.txt", "w")

#name = input("What's your name? ")

#grade = float(input("Enter your test grades: "))

#test_count = 0

#test_sum = 0;

#while grade != -1:
#	test_count = test_count+1
#	test_sum = test_sum + grade
#	grade = float(input("Enter your test grades: "))


#f.write(name+"\n===============================================================================\n Average: "+str(grade))
