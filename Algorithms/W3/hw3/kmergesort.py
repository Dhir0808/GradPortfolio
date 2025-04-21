import heapq

def merge_k_sorted(lists):
    # Merge k sorted lists using a min-heap.
    heap = []
    result = []
    
    # Initialize heap with first element from each list
    # Store (value, list_index, element_index)
    for i, lst in enumerate(lists):
        if lst:  # if list is not empty
            heapq.heappush(heap, (lst[0], i, 0))
    
    # Keep popping smallest element and add next element from same list
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))
    
    return result

def kmergesort(lst, k):
    # Sort list using k-way mergesort
    n = len(lst)
    if n <= 1:
        return lst
    
    # Split list into k parts
    sublists = []
    size = (n + k - 1) // k  # ceiling division
    for i in range(0, n, size):
        sublist = lst[i:i + size]
        sublists.append(kmergesort(sublist, k))
    
    # Merge k sorted sublists
    return merge_k_sorted(sublists)
