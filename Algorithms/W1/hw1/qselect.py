import random


def qselect(k, a):
    i = random.randrange(len(a))
    a[0], a[i] = a[i], a[0]
    pivot = a[0] 
    left = [x for x in a if x < pivot]
    remaining = k - len(left) - 1 # 1 is for pivot
    if remaining <= 0: # cases 1-2: no need to do right!
        return pivot if remaining == 0 else qselect(k, left)
    right = [x for x in a[1:] if x >= pivot]
    return qselect(remaining, right) # case 3

# Derving Complexities for Best Case and Worst Case
# Best Case: O(n)
# Everytime the pivot splits the array in half -> n + n/2 + n/4 + n/8 + ... = O(n) -> every node visited once
# Worst Case: O(n^2)
# Everytime the pivot is the smallest or largest element -> T(n) = T(n-1) + O(n) -> O(n^2) 

# print(qselect(2, [1,2,3,4,5,6,7,8,9,10]))