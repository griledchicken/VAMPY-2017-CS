con = {}
con["Joj"]     = []
con["Emily"]   = ["Joj", "Jeph", "Jeff"]
con["Jeph"]    = ["Joj", "Geoff"]
con["Jeff"]    = ["Joj", "Judge"]
con["Geoff"]   = ["Joj", "Jebb"]
con["Jebb"]    = ["Joj", "Emily"]
con["Judge"]   = ["Joj", "Judy"]
con["Jodge"]   = ["Joj", "Jebb", "Stephan", "Judy"]
con["Judy"]    = ["Joj", "Judge"]
con["Stephan"] = ["Joj", "Jodge"]

names = ["Joj", "Jeph", "Jeff", "Jebb", "Stephan", "Judy", "Emily", "Geoff", "Judge", "Jodge"]

candidate = names[0]
for i in range(1, len(names)):
	if names[i] in con[candidate]:
		candidate = names[i]

print("Our best candidate is {0}".format(candidate))

print("Verifying the candidate 1/2...")
for name in names:
	if name in con[candidate]:
		print("The candidate is a lie! They know somebody!")
		exit()
	elif name != candidate and name not in con[name]:
		print("The celebrity is a lie! They are not known by somebody!")
		exit()

print("We made it to the end, and the celebrity is the real deal!")
