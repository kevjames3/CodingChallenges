import sys

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
