import sys

def longestCommonSubsequence(x, y):
    return x

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: LongestCommonSubsequence.py [File] [?'Testing']"
        sys.exit(1)

    filepath = sys.argv[1]
    testing = (True if sys.argv[2] == "Testing" else False)  

    fileHandle = open(filepath, 'r')
    for line in fileHandle:
        test, answer = map(str.strip, line.split("#"))  
        x,y = map(str.strip, test.split(";"))
        if testing:
            print "Output: '%s', Answer: '%s'" % (longestCommonSubsequence(x, y), answer)
        else:
            print longestCommonSubsequence(x, y)

    sys.exit(0)
