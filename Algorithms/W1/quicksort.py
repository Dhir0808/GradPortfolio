import random


def qsort(arr):
    if len(arr) <= 1:
        return arr
    i = random.randrange(len(arr))
    arr[0], arr[i] = arr[i], arr[0]
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return qsort(left) + [pivot] + qsort(right)

print(qsort([3, 6, 8, 10, 1, 2, 1]))