import random, time
# implementation of binary search algo
# binary is faster than naive
# naive search will scan entire list looking for its target
# if it find the target returns the index and if not found return -1

def naive_search(l, target):
    # ex: l = [1, 3, 10, 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1













# binary search uses divide and conquer and leverages the fact that a given list is SORTED

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    if high < low:
        return -1

    # example l = [1,3,5,10,12] and we are looking to return 3
    midpoint = (low + high) // 2 #2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else:
        #target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)

if __name__=='__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l,target))
    print(binary_search(l,target))


    length = 10000
    # build a sorted list of length 10000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list = sorted(list(sorted_list))

    start = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    end = time.time()
    print("Naive search time: ", (end - start)/length, "seconds")

    start = time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    end = time.time()
    print("Binary search time: ", (end - start)/length, "seconds")





# results:  
# 3
# 3
# Naive search time:  0.0002749797344207764 seconds
# Binary search time:  5.4954767227172855e-06 seconds












