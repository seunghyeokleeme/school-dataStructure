def shellShort(A):
    H = gapSequence(len(A))
    for h in H:
        for k in range(H):
            stepInsertionSort(A, k, h)

def stepInsertionSort(A, k:int, h:int):
    for i in range(k+h, len(A), h):
        j = i - h
        newItem = A[i]
        while 0 <= j and newItem < A[j]:
            A[j+h] = A[j]
            j -= h
        A[j+h] = newItem

def gapSequence(n:int) -> list:
    H = [1]; gap = 1
    while gap < n / 5:
        gap = 3 * gap +1
        H.append(gap)
    H.reverse()
    return H