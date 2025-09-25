# Write your program here
inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")

inputFile = open(inputFileName, 'r')
outputFile = open(outputFileName, 'w')

lineNumber = 0
for line in inputFile:
    lineNumber += 1
    outputFile.write("%4d> %s" % (lineNumber, line))

outputFile.close()