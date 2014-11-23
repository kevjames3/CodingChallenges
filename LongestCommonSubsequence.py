import sys

'''
Algorithm defined by mathamatical description from here:
http://en.wikipedia.org/wiki/Longest_common_subsequence_problem#LCS_function_defined
'''
def longestCommonSubsequence(x, y):
    if len(x) == 0 or len(y) == 0:
        return ""

    print "X: '%s', Y: '%s' " % (x,y)

    x_i = x[-1]
    y_i = y[-1]

    if x_i == y_i:
        return longestCommonSubsequence(x[:-1], y[:-1]) + x_i
    else:
        result_x_minus_one = longestCommonSubsequence(x[:-1], y)
        result_y_minus_one = longestCommonSubsequence(x, y[:-1])
        if len(result_x_minus_one) >= len(result_y_minus_one):
            return result_x_minus_one
        else:
            return result_y_minus_one

def processFile(fileHandle):
    for line in fileHandle:
        if not line.strip():
            continue;
        
        x,y = map(str.strip, line.split(";"))

        if len(x) > 50 or len(y) > 50:
            #This is based on the requirement in the document
            continue

        print longestCommonSubsequence(x, y)

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: LongestCommonSubsequence.py [File] [?'Testing']"
        sys.exit(1)

    filepath = sys.argv[1]
    testing = (True if len(sys.argv) == 3 and sys.argv[2] == "Testing" else False)  

    fileHandle = open(filepath, 'r')
    processFile(fileHandle)
    fileHandle.close()
