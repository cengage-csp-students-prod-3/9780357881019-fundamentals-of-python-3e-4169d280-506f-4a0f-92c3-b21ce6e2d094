import random
def shuffleString(theString):
    chars = list(theString)          
    random.shuffle(chars)            
    print("".join(chars))            
shuffleString("Apples are red")