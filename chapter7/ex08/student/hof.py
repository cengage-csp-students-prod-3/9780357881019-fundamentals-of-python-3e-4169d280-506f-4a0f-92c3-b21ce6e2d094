# Write your code here
def myMap(func, lst):
    """Applies func to each element of lst and returns a new list."""
    result = []
    for item in lst:
        result.append(func(item))
    return result


def myFilter(func, lst):
    """Returns a list of elements from lst for which func(item) is True."""
    result = []
    for item in lst:
        if func(item):
            result.append(item)
    return result


def myReduce(func, lst):
    """Applies func cumulatively to the items of lst, reducing to a single value."""
    if not lst:
        raise TypeError("myReduce() of empty sequence with no initial value")
    
    result = lst[0]
    for item in lst[1:]:
        result = func(result, item)
    return result