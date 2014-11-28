import sys

def getCombinationsOfOperators(places):
    validOperatiors = ['+', '-', '']
    returnedCombinations = []

    if places == 0:
        return ['']
    elif places == 1: #We reached the bottom of the stack
        for operator in validOperatiors:
            returnedCombinations.append([operator])
    else:
        for operator in validOperatiors:
            children = getCombinationsOfOperators(places - 1)
            for child in children:
                returnedCombinations.append([operator] + child)

    return returnedCombinations

def isUgly(expression):
    divisbleNumbers = [2,3,5,7]
    finalValue = eval(expression)

    isUgly = False
    if finalValue != 1 and finalValue != 0:
        for num in divisbleNumbers:
            if finalValue % num:
                isUgly = True

    return isUgly

def combinationsOfBadValues(value):
    operatorCombinations = getCombinationsOfOperators(len(str(value)) - 1)
    combosUgly = 0

    for combo in operatorCombinations:
        expression = str(value[0])
        currIndex = 1
        for operator in combo:
            expression += operator
            expression += str(value[currIndex])
            currIndex += 1

        if isUgly(expression):
            combosUgly += 1

    return combosUgly
    
def processFile(fileHandle):
    for line in fileHandle:
        if not line.strip():
            continue;
        
        print combinationsOfBadValues(line.strip())

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: BadNumbers.py [File]"
        sys.exit(1)

    filepath = sys.argv[1]

    fileHandle = open(filepath, 'r')
    processFile(fileHandle)
    fileHandle.close()
