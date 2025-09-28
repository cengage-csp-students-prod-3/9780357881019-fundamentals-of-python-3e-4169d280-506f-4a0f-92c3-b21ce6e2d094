# Write your program here
code = input("Enter the coded text: ")

wordList = code.split()
plainText = ""

for word in wordList:

    word = word[-1] + word[:-1]

    decimal = 0
    exponent = len(word) - 1
    for digit in word:
        decimal = decimal + int(digit) * 2**exponent
        exponent = exponent - 1

    decimal -= 1

    plainText += chr(decimal)

print(plainText)