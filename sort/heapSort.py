def heapSort(A):
    buildHeap(A)
    for last in range(len(A)-1, 0, -1):
        A[last], A[0] = A[0], A[last]
        percolateDown(A, 0, last-1)

def buildHeap(A):
    for i in range((len(A)-2) // 2, -1, -1):
        percolateDown(A, i, len(A)-1)

def percolateDown(A, k:int, end:int):
    child = k * 2 + 1
    right = k* 2 + 2
    if child <= end:
        if right <= end and A[child] > A[right]:
            child = right
        if A[k] < A[child]:
            A[k], A[child] = A[child], A[k]
            percolateDown(A, child, end)