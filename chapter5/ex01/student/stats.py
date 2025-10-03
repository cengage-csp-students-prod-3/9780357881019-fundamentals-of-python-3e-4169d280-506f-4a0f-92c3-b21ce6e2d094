# Write your program here
def mean(numberList):
    sum = 0
    for number in numberList:
        sum += number

    if len(numberList) == 0:
        return 0
    else:
        return sum / len(numberList)
    
def median(numberList):
    numbers = []
    for number in numberList:
        numbers.append(number)

    numbers.sort()
    if len(numberList) == 0:
        return 0
    else:
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 2:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1])/2
        
def mode(numberList):
    theDictionary = {}
    for number in numberList:
        freq = theDictionary.get(number, None)
        if freq == None:
            theDictionary[number] = 1
        else:
            theDictionary[number] = freq + 1

    if len(theDictionary) == 0:
        return 0
    else:
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key    

def main():
    numberList = (3, 1, 7, 1, 4, 10)
    print("test")
    print("List:", numberList)
    print("Median:", median(numberList))
    print("Mode:", mode(numberList))
    print("Mean:", mean(numberList))

if __name__ == "__main__":
    main()