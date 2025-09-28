inputFileName = input("Enter the input file name: ")
outputFileName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

inputFile = open(inputFileName, 'r')
code = inputFile.read()

outFile = open(outputFileName, 'w')

plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue = 127 - \
                        (distance - (1 - ordValue))
    plainText += chr(cipherValue)

outFile.write(plainText)
outFile.close()