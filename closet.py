id = 0
tops = ["Vampy","Skiing","Meteor Cats","Colombia","Home"]
bottoms = ["Khul","Khaki","Athletic shorts","Sweats"]
shoes = ["Converse","Running"]
headgear = ["Baseball cap","Sunglasses","combo","None","none","NONE","NoNe","nOnE"]
socks = ["Black","feetures!","White","wool"]

pattern = "#{0}: Top={1}, Bottom={2}, Shoes={3}, Headgear={4}, Socks={5}"

for top in tops:
	for bottom in bottoms:
		for kicks in shoes:
			for headitem in headgear:
				for pair in socks:
					id += 1
					print(pattern.format(id, top, bottom, kicks, headitem, pair))

