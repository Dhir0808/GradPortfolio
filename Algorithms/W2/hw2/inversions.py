def merge_and_count(left, right, inv_count):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            # When an element from right is smaller, all remaining elements
            # in left form inversions with this element
            result.append(right[j])
            inv_count += len(left) - i
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inv_count

def mergesort_and_count(lst):
    if len(lst) <= 1:
        return lst, 0
        
    mid = len(lst) // 2
    left, left_inv = mergesort_and_count(lst[:mid])
    right, right_inv = mergesort_and_count(lst[mid:])
    merged, merge_inv = merge_and_count(left, right, 0)
    
    return merged, left_inv + right_inv + merge_inv

def num_inversions(lst):
    _, inv_count = mergesort_and_count(lst)
    return inv_count
