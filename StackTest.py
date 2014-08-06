import sys

def printEveryOtherNumber(array):
	print array

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Bad number of arguments!"
		exit(-1)

	fileName = sys.argv[1]
	with open(fileName, 'r') as f:
		for line in f:
			array = map(int, line.split(" ")) #turn all string numbers into 
			printEveryOtherNumber(array)