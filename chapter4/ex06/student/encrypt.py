# Write your program here
plainText = input("Enter a message: ")

code = ""

for ch in plainText:
    ordValue = ord(ch) + 1

    binaryString = ""
    while ordValue > 0:
        remainder = ordValue % 2
        ordValue = ordValue // 2
        binaryString = str(remainder) + binaryString

    if len(binaryString) > 1:
        binaryString = binaryString[1:] + binaryString[0]

    code += binaryString + " "

print(code)