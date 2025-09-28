# Write your program here

inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")

inputFile = open(inputFileName, 'r')
text = inputFile.read()

outFile = open(outputFileName, 'w')
outFile.write(text)
outFile.close()