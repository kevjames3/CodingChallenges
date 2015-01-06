import sys
import re
import math
import time

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

def getCombinationsOfOperators(places):
    returnedCombinations = []

    if places == 0:
        return ['']
    elif places == 1: #We reached the bottom of the stack
        for operator in ['+', '-', '']:
            returnedCombinations.append([operator])
    else:
        for operator in ['+', '-', '']:
            children = getCombinationsOfOperators(places - 1)
            for child in children:
                returnedCombinations.append([operator] + child)

    return returnedCombinations

def combinationsOfBadValues(expression):
    if len(expression) == 0:
        return 0
    elif len(expression) == 1:
        return 1 if isUgly(expression) else 0
    else:
        return combinationsOfBadValues_Helper(expression, 1)

def combinationsOfBadValues_Helper(expression, operatorPosition):
    if(operatorPosition >= len(expression)):
        tokenizedExpression = re.split("(\+|-)", expression)
        originalExpression = expression
        expression = "" #reset the expression, as we will re-add to it
        for token in tokenizedExpression:
            if re.match("\d+", token):
                token = str(int(token))
            expression += token

        #print "Expression: %s, IsUgly: %s" % (originalExpression, isUgly(expression))
        return 1 if isUgly(expression) else 0
    else:
        combinations = 0
        nextChar = expression[operatorPosition:][0:1] #Peek at the next char, see if it is a 00

        skipNumericalOperators = False #We will be skipping loop iterations if the next char is '0' as +0 == -0
        numericalOperators = ['+', '-']
        nonOperators = ['']
        operators = nonOperators + numericalOperators

        for operator in operators: 
            if skipNumericalOperators and operator in numericalOperators:
                continue 

            combinationsFromExpression = 0

            newExpression = expression[0:operatorPosition] + operator + expression[operatorPosition:]
            offsetDueToNewCharacter = 1 + (0 if operator == "" else 1)
            combinationsFromExpression = combinationsOfBadValues_Helper(newExpression, operatorPosition + offsetDueToNewCharacter)

            if nextChar is "00" and operator in numericalOperators:
                combinationsFromExpression *= 2 * (len(numericalOperators) - 1)
                skipNumericalOperators = True   

            combinations += combinationsFromExpression

        return combinations

def combinationsOfBadValues_Gold(value):    
    spacesForOperators = len(str(value)) - 1

    operatorCombinations = getCombinationsOfOperators(spacesForOperators)
    combosUgly = 0

    for combo in operatorCombinations:
        #Create the expression
        expression = ""
        currIndex = 0

        if len(combo) < len(value):
            expression = str(value[0])
            currIndex = 1

        for operator in combo:
            expression += operator
            expression += str(value[currIndex])
            currIndex += 1

        #Make sure all items in the list are parsible as ints
        tokenizedExpression = re.split("(\+|-)", expression)
        originalExpression = expression
        expression = "" #reset the expression, as we will re-add to it
        for token in tokenizedExpression:
            if re.match("\d+", token):
                token = str(int(token))
            expression += token

        #Now check if it is ugly
        #print "Expression: %s, IsUgly: %s" % (originalExpression, isUgly(expression))
        if isUgly(expression):
            combosUgly += 1

    return combosUgly
    
def processFile(fileHandle):
    for line in fileHandle:
        if not line.strip():
            continue;
        
        t0 = time.clock()
        print "For line: %s" % line.strip()
        print "Optimized Value: %d, Time %2.2f" % (combinationsOfBadValues(line.strip()), time.clock() - t0)
        t0 = time.clock()
        print "Gold Value: %d, Time %2.2f" % (combinationsOfBadValues_Gold(line.strip()), time.clock() - t0)
        print "----"

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: BadNumbers.py [File]"
        sys.exit(1)

    filepath = sys.argv[1]

    fileHandle = open(filepath, 'r')
    processFile(fileHandle)
    fileHandle.close()
