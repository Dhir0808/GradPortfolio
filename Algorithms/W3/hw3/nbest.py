import heapq
from itertools import product

def nbesta(a, b):
    # Algorithm (a): Generate all pairs, sort, take top n. O(n^2 log(n^2))
    pairs = [(x, y) for x in a for y in b]
    pairs.sort(key=lambda p: (p[0] + p[1], p[1]))
    return pairs[:len(a)]

def quickselect(arr, k, key=lambda x: x):
    # Helper function for nbestb: find kth smallest element
    if not arr:
        return []
    
    pivot = arr[len(arr)//2]
    left = [x for x in arr if key(x) < key(pivot)]
    equal = [x for x in arr if key(x) == key(pivot)]
    right = [x for x in arr if key(x) > key(pivot)]
    
    if k < len(left):
        return quickselect(left, k, key)
    elif k < len(left) + len(equal):
        return arr[:k]
    else:
        return left + equal + quickselect(right, k - len(left) - len(equal), key)

def nbestb(a, b):
    # Algorithm (b): Generate all pairs, use quickselect. O(n^2)
    pairs = [(x, y) for x in a for y in b]
    return quickselect(pairs, len(a), key=lambda p: (p[0] + p[1], p[1]))

def nbestc(a, b):
    # Algorithm (c): Best-first search using heap. O(n log n)
    if not a or not b:
        return []
        
    n = len(a)
    # Sort both lists
    a.sort()
    b.sort()
    
    # Priority queue stores (sum, y, x_idx, y_idx) to match required ordering
    # where (x,y) < (x',y') iff x+y < x'+y' or (x+y==x'+y' and y<y')
    heap = [(a[0] + b[0], b[0], 0, 0)]
    seen = {(0, 0)}
    result = []
    
    while len(result) < n and heap:
        _, _, x_idx, y_idx = heapq.heappop(heap)
        result.append((a[x_idx], b[y_idx]))
        
        # Try next element in b
        if y_idx + 1 < n and (x_idx, y_idx + 1) not in seen:
            next_y = b[y_idx + 1]
            heapq.heappush(heap, (a[x_idx] + next_y, next_y, x_idx, y_idx + 1))
            seen.add((x_idx, y_idx + 1))
            
        # Try next element in a
        if x_idx + 1 < n and (x_idx + 1, y_idx) not in seen:
            next_x = a[x_idx + 1]
            heapq.heappush(heap, (next_x + b[y_idx], b[y_idx], x_idx + 1, y_idx))
            seen.add((x_idx + 1, y_idx))
    
    return result
