# Write your program here
inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

inputFile = open(inputFileName, 'r')
plainText = inputFile.read()

outputFile = open(outputFileName, 'w')

code = ''
for ch in plainText:
    ordValue = ord(ch)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)

outputFile.write(plainText)
outputFile.close()