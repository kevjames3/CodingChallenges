'''
Focus of this file is to determine the sum of the first 1000 prime numbers.
'''
import random
import math

def isPrime(num):
	result = True
	if num > 2 and not (num % 2 == 0):
		#Use Fermat's little theorem a^n (mod n) = a (mod n).
		#If they equal each other, then that means that this 
		#one is prime.  Also, 2 <= a < n where a is an integer 
		a = random.randint(2, num - 1)
		if ((a ** num) % num) == (a % num):
			sqrt_n = math.sqrt(num)
			for divider in range(3, int(math.ceil(sqrt_n) + 1)):
				if num % divider == 0:
					result = False
					break
		else:
			result = False

	elif not num == 2:
		result = False 
	
	return result

if __name__ == '__main__':
	primeList = []
	currentNumber = 0
	while len(primeList) < 1000:
		if isPrime(currentNumber):
			primeList.append(currentNumber)
		currentNumber += 1

	print sum(primeList)