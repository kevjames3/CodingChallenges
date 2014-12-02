import sys
import re
import math

VALID_OPERATORS = ['+', '-', '']

def getCombinationsOfOperators(places):
    returnedCombinations = []

    if places == 0:
        return ['']
    elif places == 1: #We reached the bottom of the stack
        for operator in VALID_OPERATORS:
            returnedCombinations.append([operator])
    else:
        for operator in VALID_OPERATORS:
            children = getCombinationsOfOperators(places - 1)
            for child in children:
                returnedCombinations.append([operator] + child)

    return returnedCombinations

def isUgly(expression):
    divisbleNumbers = [2,3,5,7]
    finalValue = eval(expression)
    isUgly = False

    if finalValue == 0:
        isUgly = True
    else:
        for num in divisbleNumbers:
            if not finalValue % num:
                isUgly = True

    return isUgly

def combinationsOfBadValues(value):
    #Count how many times zeros occur, because we are going to need to compensate 
    #if we account for optimizations
    additionalCombinationsIfUgly = 0
    for group in re.compile('(0{2,})').findall(value):
        numOfZeros = len(group)
        additionalCombinationsIfUgly += int(math.pow(len(VALID_OPERATORS), numOfZeros - 1))

    value = re.sub('0{2,}', '0', value) #Remove the case of two or more zeros for optimizations.
    operatorCombinations = getCombinationsOfOperators(len(str(value)) - 1)
    combosUgly = 0

    for combo in operatorCombinations:
        #Create the expression
        expression = str(value[0])
        currIndex = 1
        for operator in combo:
            expression += operator
            expression += str(value[currIndex])
            currIndex += 1

        #Make sure all items in the list are parsible as ints
        tokenizedExpression = re.split("(\+|-)", expression)
        expression = "" #reset the expression, as we will re-add to it
        for token in tokenizedExpression:
            if re.match("\d+", token):
                token = str(int(token))
            expression += token

        #Now check if it is ugly
        if isUgly(expression):
            combosUgly += 1 * additionalCombinationsIfUgly

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
