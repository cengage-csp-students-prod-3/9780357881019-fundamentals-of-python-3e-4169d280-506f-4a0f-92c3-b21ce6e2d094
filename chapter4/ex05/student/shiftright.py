# Write your program here
bits = input("Enter a string of bits: ")
if(len(bits) > 1):
    bits = bits[-1] + bits[:-1]

print(bits)