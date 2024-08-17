def quickSort(A, p:int, r:int):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)

def partition(A, p:int, r:int) -> int:
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] < x:
            i+=1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1