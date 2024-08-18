import math
from insertionSort import insertionSort

def bucketSort(A):
    n = len(A)
    B = [[] for _ in range(n)]
    
    for i in range(n):
        B[math.floor(n*A[i])].append(A[i])
    A.clear()
    for i in range(n):
        insertionSort(B[i])
        A.extend(B[i])