# Write your code here
from hof import myMap, myFilter, myReduce
from functools import reduce

def square(x): return x ** 2
def isOdd(x): return x % 2 == 1
def add(x, y): return x + y

test_lists = [
    [0, 1, 2, 3, 4],
    [3],
    []
]

for lst in test_lists:
    print("Argument list:  ", lst)

    # --- map test ---
    print("map with ** 2  :", list(map(square, lst)))
    print("myMap with ** 2:", myMap(square, lst))

    # --- filter test ---
    print("filter with odd  :", list(filter(isOdd, lst)))
    print("myFilter with odd:", myFilter(isOdd, lst))

    # --- reduce test ---
    if lst:
        print("reduce with +   :", reduce(add, lst))
        print("myReduce with + :", myReduce(add, lst))
    else:
        print("reduce with +   : []")
        print("myReduce with + : []")

    print()