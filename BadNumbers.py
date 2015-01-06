import sys
import re
import math

VALID_OPERATORS = ['+', '-', '']

def combinationsOfBadValues_Contained(expression):
    if len(expression) == 0:
        return 0
    elif len(expression) == 1:
        return 1 if isUgly(expression) else 0
    else:
        return combinationsOfBadValues_Contained_Helper(expression, 1)

def combinationsOfBadValues_Contained_Helper(expression, operatorPosition):
    if(operatorPosition >= len(expression)):
        tokenizedExpression = re.split("(\+|-)", expression)
        expression = "" #reset the expression, as we will re-add to it
        for token in tokenizedExpression:
            if re.match("\d+", token):
                token = str(int(token))
            expression += token

        #print "Expression: %s, IsUgly: %s", (expression, isUgly(expression))
        return 1 if isUgly(expression) else 0
    else:
        combinations = 0
        for operator in VALID_OPERATORS:
            newExpression = expression[0:operatorPosition] + operator + expression[operatorPosition:]
            operatorOffset = 1 + (0 if operator == "" else 1)
            combinations += combinationsOfBadValues_Contained_Helper(newExpression, operatorPosition + operatorOffset)

        return combinations

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
        for operator in VALID_OPERATORS:
            returnedCombinations.append([operator])
    else:
        for operator in VALID_OPERATORS:
            children = getCombinationsOfOperators(places - 1)
            for child in children:
                returnedCombinations.append([operator] + child)

    return returnedCombinations

def combinationsOfBadValues(value):    
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
        expression = "" #reset the expression, as we will re-add to it
        for token in tokenizedExpression:
            if re.match("\d+", token):
                token = str(int(token))
            expression += token

        #Now check if it is ugly
        #print "Expression: %s, IsUgly: %s", (expression, isUgly(expression))
        if isUgly(expression):
            combosUgly += 1

    return combosUgly
    
def processFile(fileHandle):
    for line in fileHandle:
        if not line.strip():
            continue;
        
        print "Contained Recursive: %d" % (combinationsOfBadValues_Contained(line.strip()))
        print "Old Recursive: %d" % (combinationsOfBadValues(line.strip()))

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: BadNumbers.py [File]"
        sys.exit(1)

    filepath = sys.argv[1]

    fileHandle = open(filepath, 'r')
    processFile(fileHandle)
    fileHandle.close()
