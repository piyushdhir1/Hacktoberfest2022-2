# return true if the number is prime
def isPrime(num):
	# 1,2,3 are prime
	if (num>3):
		# only check the odd numbers
		if (num%2 == 0):
			return False
		else:
			for i in range(3, (num/2)+1, 2):
				if (num%i) == 0:
					return False

	return True

# return all the primes up to a certain number
def primes(num):
	primes = []
	if (num>3):
		primes.append(1), primes.append(2), primes.append(3)

	for i in range(1, num+1, 2):
		# if 1 and 3 are in the list, don't add them again
		if ((primes[0]== 1 and primes[2] == 3) and (i==1 or i==3)):
			pass
		else:
			if isPrime(i):
				primes.append(i)
	return primes

num = 121
nums = primes(num)
print nums
