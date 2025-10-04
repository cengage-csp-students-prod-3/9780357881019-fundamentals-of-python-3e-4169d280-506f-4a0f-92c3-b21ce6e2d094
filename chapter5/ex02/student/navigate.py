# Write your program here
inputFileName = input("Enter the input file name: ")

inputFile = open(inputFileName, 'r')
lines = []

for line in inputFile:
    lines.append(line)

while True:
    print("The file has ", len(lines), "lines.")
    if len(lines) == 0:
        break
    
    lineNumber = int(input("Enter a line number [0 to quit]: "))

    if lineNumber == 0:
        break
    elif lineNumber >= len(lines):
        print("Error: line number must be less than", len(lines))
    else:
        print(lineNumber, ":", lines[lineNumber])