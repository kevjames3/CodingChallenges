'''
Run with one command line argument: the file that will be have every other number printed.
In this case, this file will be StackTestSample.txt

Example: python StackTest.py StackTestSample.txt
'''

import sys

def printEveryOtherNumber(array):
	string = ""
	for i in range(0, len(array)):
		itemPopped = array.pop()
		if i % 2 == 0:
			string = string + str(itemPopped) + " "

	print string.strip()


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Bad number of arguments!"
		exit(-1)

	fileName = sys.argv[1]
	with open(fileName, 'r') as f:
		for line in f:
			array = map(int, line.split(" ")) #turn all string numbers into 
			printEveryOtherNumber(array)