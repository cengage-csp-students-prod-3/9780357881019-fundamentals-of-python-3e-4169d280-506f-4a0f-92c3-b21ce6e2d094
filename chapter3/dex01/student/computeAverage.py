count = 1
total = 0
while count <= 10:
    score = int(input("Enter test score number " + str(count) + ": "))
    total = total + score
    if count != 10:
        count = count + 1
    else:
        break

average = total / (count)
print("The average test score is", average)