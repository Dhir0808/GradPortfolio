def qsort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [qsort2(left)] + [pivot] + [qsort2(right)]

# in the next functions that I created the tree is of the form [left_subtree, value, right_subtree]
def sorted(t):
    if t == []:
        return []
    return sorted(t[0]) + [t[1]] + sorted(t[2])

def _search(t, x):
   
    if t == []:
        return t
    if x == t[1]:
        return t
    elif x < t[1]:
        return _search(t[0], x)
    else:
        return _search(t[2], x)

def search(t, x):

    result = _search(t, x)
    return result != [] and result[1] == x

def insert(t, x):

    if t == []:
        t.extend([[], x, []]) # extend is better than append because it is more efficient, extend is equivalent to += -> Will be asked in quiz
        return t
    
    target = _search(t, x)
    if target == []:
        target.extend([[], x, []])
    return t

# Complexities for the functions

# Function          Best Case       Worst Case

# qsort             O(n)            O(n^2)
# sorted            O(n)            O(n)
# _search           O(log n)        O(n)
# search            O(log n)        O(n)
# insert            O(log n)        O(n)