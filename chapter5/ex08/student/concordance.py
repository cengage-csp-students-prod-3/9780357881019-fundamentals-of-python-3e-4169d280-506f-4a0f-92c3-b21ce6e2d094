fileName = input("Enter the input file name: ")
uniqueWords = {}

inputFile = open(fileName, 'r')

for line in inputFile:
    words = line.split()
    for word in words:
        frequency = uniqueWords.get(word, None)
        if frequency == None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = frequency + 1

words_list = list(uniqueWords.keys())
words_list.sort()
for word in words_list:
    print(word, uniqueWords[word])