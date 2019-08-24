import heapq

# O(n + k*ln(n))
def heap_find_naive(arr, k):
    # O(n)
    heapq.heapify(arr)

    # O(k)
    for _ in range(k):
        # O(ln(n))
        heapq.heappop(arr)

    return arr[0]

# O(n*ln(k))
def heap_find(arr, k):
    heap = []

    for x in arr:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heappush(heap, x)
            heapq.heappop(heap)
    
    return heap[0]

#print(sorted(arr))

for k in range(9):
    arr = [0, 5, 8, 3, 2, 3, 5, 8, 6]
    print(heap_find(arr, k+1))