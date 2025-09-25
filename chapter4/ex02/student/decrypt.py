# Write your program here
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ""

for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
    if cipherValue < 0:
        cipherValue = 127 - (distance - (1 - ordValue))
    plainText += chr(cipherValue)

print(plainText)