import sys

'''
Algorithm defined by mathamatical description from here:
http://en.wikipedia.org/wiki/Longest_common_subsequence_problem#LCS_function_defined
'''
def longestCommonSubsequence(x, y, graph):
    if len(x) == 0 or len(y) == 0:
        return ""

    if graph[x][y] is not None:
        return graph[x][y]

    x_i = x[-1]
    y_i = y[-1]

    if x_i == y_i:
        return longestCommonSubsequence(x[:-1], y[:-1], graph) + x_i
    else:
        result_x_minus_one = longestCommonSubsequence(x[:-1], y, graph)
        result_y_minus_one = longestCommonSubsequence(x, y[:-1], graph)
        if len(result_x_minus_one) >= len(result_y_minus_one):
            graph[x][y] = result_x_minus_one
            return result_x_minus_one
        else:
            graph[x][y] = result_y_minus_one
            return result_y_minus_one

def processFile(fileHandle):
    for line in fileHandle:
        if not line.strip():
            continue;
        
        x,y = map(str.strip, line.split(";"))

        #Construct the graph to stop backtracking
        graph = {}
        x_counter = 0
        while x_counter <= len(x):
            graph[x[0:x_counter]] = {}
            y_counter = 0
            while y_counter <= len(y):
                graph[x[0:x_counter]][y[0:y_counter]] = None
                y_counter += 1
            x_counter += 1


        print longestCommonSubsequence(x, y, graph)

if __name__ == '__main__':
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print "Incorrect command line arguments"
        print "Useage: LongestCommonSubsequence.py [File]"
        sys.exit(1)

    filepath = sys.argv[1]

    fileHandle = open(filepath, 'r')
    processFile(fileHandle)
    fileHandle.close()
