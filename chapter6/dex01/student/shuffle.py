import random
def shuffleString(theString):
    print("".join(random.shuffle(list(theString))))
shuffleString("Apples are red")