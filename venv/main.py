
def squares():

    squared = [x**2 for x in range(1,11)]
    print(squared)
    return squared

def multiples(arg):
    #returns arg multiple of all numbers in range [0,100), where "[]" denotes inclusive and "()" exclusive
    multi = [x * arg for x in range(0,100)]
    print(multi)
    return


def sum_lists(arg1,arg2):
    """Return a list that is the element-wise sum of the elements of the
    two lists of equal size passed as arguments.
    #IMPLEMENTATION NOTE: Uses Assertionerror instead of ValueError as this error seems more appropriate
    """
    try:
        assert len(arg1) == len(arg2), 'Lists not of equal length'
    except AssertionError as e:
        print(e)
        exit()
    list_of_sums = [x+y for x,y in zip(arg1,arg2)]
    print(list_of_sums)
    return list_of_sums

sum_lists([1,2],[1,2])