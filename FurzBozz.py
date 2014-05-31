'''
INPUT SAMPLE:

Your program should read an input file (provided on the command line) which contains multiple newline separated lines. 
Each line will contain 3 numbers which are space delimited. The first number is first number to divide by ('A' in this example), 
the second number is the second number to divide by ('B' in this example) and the third number is where you should count till 
('N' in this example). You may assume that the input file is formatted correctly and is the numbers are valid positive integers. E.g.

3 5 10
2 7 15

OUTPUT SAMPLE:

Print out the series 1 through N replacing numbers divisible by 'A' by F, numbers divisible by 'B' by B and numbers divisible by both as 'FB'. Since the input file contains multiple sets of values, your output will print out one line per set. Ensure that there are no trailing empty spaces on each line you print. E.g.

1 2 F 4 B F 7 8 F B
1 F 3 F 5 F B F 9 F 11 F 13 FB 15
'''

import sys

class FizzBuzz:
	def __init__(self, a, b, n):
		self.a = a
		self.b = b
		self.n = n

	def playGame(self):
		outputFromGame = []
		for counter in range(1, 1 + self.n):
			if(counter % self.a == 0 and counter % self.b == 0):
				outputFromGame.append('FB')
			elif(counter % self.a == 0):
				outputFromGame.append('F')
			elif(counter % self.b == 0):
				outputFromGame.append('B')
			else:
				outputFromGame.append(counter)

		outputFromGame = map(str, outputFromGame)
		return " ".join(outputFromGame)

if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise Exception("We need a file path to where we can read in these numbers")

	filepath = sys.argv[1]
	fileHandle = open(filepath, 'r')
	for line in fileHandle:
		arguments = map(int, line.split(" "))
		print FizzBuzz(arguments[0], arguments[1], arguments[2]).playGame() 