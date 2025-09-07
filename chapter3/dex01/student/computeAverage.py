count = 1
total = 0
while count < 10:
    score = int(input("Enter test score number " + str(count) + ": "))
    total = total + score
    count = count + 1
average = total / count
print("The average test score is", average)