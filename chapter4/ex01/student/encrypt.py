# Write your program here
plainText = input("Enter a message: ")
distance = int(input("Enter the distance vaule: "))
code = ""

for char in plainText:
    ordValue = ord(char)
    cipherValue = ordValue + distance
    if cipherValue > 127:
        cipherValue = distance - (127 - ordValue + 1)
    code += chr(cipherValue)

print(code)