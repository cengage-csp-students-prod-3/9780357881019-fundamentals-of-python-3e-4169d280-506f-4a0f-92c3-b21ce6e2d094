# Write your program here
inputFileName = input("Enter the input file name: ")

inputFile = open(inputFileName, 'r')
lines = []

for line in inputFile:
    lines.append(line)

selected = []

while True:
    print("The file has ", len(lines), "lines.")
    if len(lines) == 0:
        break

    raw = input("Enter line number: [0 to quit]")
    if not raw.strip().isdigit():
        break
    
    lineNumber = int(raw)

    if lineNumber == 0:
        break
    elif lineNumber < 1 or lineNumber > len(lines):
        print("Error: line number must be less than", len(lines))
    else:
        selected.append(lines[lineNumber - 1])
        print(selected)