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

        return 1 if isUgly(expression) else 0
    else:
        combinations = 0
        nextChar = expression[operatorPosition:][0:2] #Peek at the next char, see if it is a 00

        skipNumericalOperators = False #We will be skipping loop iterations if the next chars are '00' as 0+0 == 0-0 (etc)
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

            if nextChar == "00" and operator in numericalOperators:
                combinationsFromExpression *= 2 * (len(numericalOperators) - 1)
                skipNumericalOperators = True   

            combinations += combinationsFromExpression

        return combinations

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
