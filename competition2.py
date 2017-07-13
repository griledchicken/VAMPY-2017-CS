nums = []
primes = []
splits = []
happrimes = []
numcount = int(input("How many numbers would you like to know?: "))
for f in range(numcount):
	nums.append(int(input("What is your number?: ")))
for i in range(len(nums)):
	a = 0
	b = 0
	c = 0
	d = 0
	E = 0
	prime = True
	for j in range(nums[i]):
		if j not in[0, 1]:
			if (nums[i] / j) % 1 == 0:
				happrimes.append("NO")
			else:
				primes.append(nums[i])	
	if i in primes:
		if primes[k] < 10:
			if primes[k] == 7:
				happrimes.append("YES")
			else:
				happrimes.append("NO")
		else:
			for l in range(50):
				a = primes[k] % 10
				b = (primes[k] - a)/10
				c = (primes[k]-(b+a))/100
				d = (primes[k]-(a+b+c))/1000
				e = (primes[k]-(a+b+c+d))/10000
				E = (a*a)+(b*b)+(c*c)+(d*d)
				if E == 1:
					happrimes.append("YES")
				else:
					primes.pop(k)
					primes.append(E)
					continue
			if E != 1:
				happrimes.append("NO")
	print(str(nums[int(i)])+", "+str(happrimes[int(i)]))

	
	

		

		
