import math

def radixSort(A):
    maxValue = max(A)
    numDigits = math.ceil(math.log10(maxValue))
    bucket = [[] for _ in range(10)]

    for i in range(numDigits):
        for x in A:
            y = (x // 10**i) % 10
            bucket[y].append(x)
        A.clear()
        for j in range(10):
            A.extend(bucket[j])
            bucket[j].clear()