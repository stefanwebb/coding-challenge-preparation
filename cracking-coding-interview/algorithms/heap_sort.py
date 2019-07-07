# Indexing functions
def leftChild(idx):
    return 2*idx + 1

def rightChild(idx):
    return 2*(idx + 1)

def parent(idx):
    return (idx-1)//2

# Insert an element
def insert(heap, x):
    # Add to end of heap
    heap.append(x)

    if len(heap) == 1:
        return

    # Swap until heap property restored
    thisIdx = len(heap)-1
    parentIdx = parent(thisIdx) 
    while thisIdx > 0 and heap[thisIdx] > heap[parentIdx]:
        heap[parentIdx], heap[thisIdx] = heap[thisIdx], heap[parentIdx]
        thisIdx = parentIdx
        parentIdx = parent(thisIdx)

# Remove the largest element
def extract(heap):
    ans = heap[0]

    if len(heap) == 1:
        heap.pop()
        return ans

    # Move last element to beginning
    heap[0] = heap[-1]
    heap.pop()

    # Reinstate the heap property
    thisIdx = 0
    
    while True:
        leftIdx = leftChild(thisIdx)
        rightIdx = leftIdx + 1
        largest = thisIdx

        if leftIdx < len(heap) and heap[leftIdx] > heap[largest]:
            largest = leftIdx

        if rightIdx < len(heap) and heap[rightIdx] > heap[largest]:
            largest = rightIdx

        if largest != thisIdx:
            heap[thisIdx], heap[largest] = heap[largest], heap[thisIdx]
            thisIdx = largest
        else:
            break

    return ans

# NOTE: Subtle bugs in extract() that I encountered

def heap_sort(arr):
    ans = []
    heap = []
    for x in arr:
        insert(heap, x)
    
    while len(heap):
        ans.append(extract(heap))

    return ans

arr = [7, 3, 8, 7, 2, 9, 8, 1, 0]

print(heap_sort(arr))
