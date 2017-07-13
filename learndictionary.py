import functools


#d = {"age":12}
#d["name"] = "Will"


#print(d["age"])
#print(d["name"])

#Merge 2 Dictionaries
d1 = {"key1":1, "key2":2, "key3":3}
d2 = {"key4":12, "key6":7, "key5":123}
def multiply_dictionary(dictionary, multiple):
	for key in dictionary:
		dictionary[key] *= multiple
	print(dictionary)

printable = sorted(d2)
print(str(printable))

