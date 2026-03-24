def isInt(n):
	"""
	Checks if the given number is in fact an integer
	"""
	result = ((n % 1) == 0)
	return result

def factorial(n):
	"""
	Calculate the factorial of a given number.
	
	:param int n: The factorial to calculate
	:return: The resultant factorial
	"""
	if isInt(n):
		raise ValueError('Only use integers.')
	elif n < 0:
		raise ValueError('Only use non-negative integers.')
		
	factorial = 1
	for i in range(1, n + 1):
		factorial = factorial * i
	return factorial
