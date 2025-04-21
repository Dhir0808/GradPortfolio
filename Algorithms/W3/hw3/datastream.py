import heapq

def ksmallest(k, stream):
    """Find k smallest elements in a data stream using O(k) space.
    Uses a max heap (by negating values) to maintain k smallest elements."""
    # Use a max heap of negative numbers to keep k smallest elements
    heap = []
    
    for x in stream:
        if len(heap) < k:
            # If heap has less than k elements, add new element
            heapq.heappush(heap, -x)
        elif -heap[0] > x:
            # If new element is smaller than largest in heap, replace largest
            heapq.heapreplace(heap, -x)
    
    # Convert back to positive numbers and sort ascending
    result = [-x for x in heap]
    result.sort()  # Sort in ascending order
    return result
