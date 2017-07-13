import functools
@functools.lru_cache(maxsize=None)
def gcd(a, b):
	if a < b:
		a, b = b, a

	def solver(a, b):
		if b == 0:
			return a
		else:
			return solver(b, a%b)

	return solver(a, b)
