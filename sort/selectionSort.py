def selectionSort(A):
    for last in range(len(A)-1, 0, -1):
        k = theLargest(A, last)
        A[k], A[last] = A[last], A[k]

def theLargest(A, last:int) -> int:
    largest = 0
    for i in range(last+1):
        if A[i] > A[largest]:
            largest = i
    
    return largest