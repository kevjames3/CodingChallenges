'''
Focus of this file is to determine the biggest prime palindrome under 1000.
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

def isPaladrome(string):
	return string == string[::-1]

if __name__ == '__main__':
	primeList = []
	for num in range(0, 1001):
		if isPrime(num):
			primeList.append(num)

	#List is already sorted, don't need to try anything else
	largetPalandromePrime = 0
	for prime in primeList:
		if isPaladrome(str(prime)):
			largetPalandromePrime = prime

	print largetPalandromePrime