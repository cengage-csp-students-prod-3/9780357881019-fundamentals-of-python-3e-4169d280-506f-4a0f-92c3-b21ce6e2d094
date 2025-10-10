# Write your code here
def isSorted(sort_list):

    if(len(sort_list) == 0 or len(sort_list) == 1):
        return True
    
    else: 
        for index in range(len(sort_list) - 1):
            if sort_list[index] > sort_list[index + 1]:
                return False
            
    return True

def main():

    list_1 = []
    print(isSorted(list_1))

    list_1 = [1]
    print(isSorted(list_1))

    list_1 = list(range(10))
    print(isSorted(list_1))
