# Write your program here
fileName1 = input("Enter the first file name: ")
fileName2 = input("Enter the second file name: ")

inputFile1 = open(fileName1, 'r')
inputFile2 = open(fileName2, 'r')

while True:

    line1 = inputFile1.readline()
    line2 = inputFile2.readline()

    if line1 == "" and line2 == "":
        print("Yes")
        break
    elif line1 != line2:
        print("No")
        print(line1)
        print(line2)
        break
