import sys

def getCombinationsOfOperators(places):
    validOperatiors = ['+', '-', '']
    returnedCombinations = []

    if places == 1: #We reached the bottom of the stack
        for operator in validOperatiors:
            returnedCombinations.append([operator])
    else:
        for operator in validOperatiors:
            children = getCombinationsOfOperators(places - 1)
            for child in children:
                returnedCombinations.append([operator] + child)

    return returnedCombinations

def combinationsOfBadValues(value):
    return None
    
def processFile(fileHandle):
    for line in fileHandle:
        if not line.strip():
            continue;
        
        print combinationsOfBadValues(line)

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: BadNumbers.py [File]"
        sys.exit(1)

    filepath = sys.argv[1]

    fileHandle = open(filepath, 'r')
    processFile(fileHandle)
    fileHandle.close()
