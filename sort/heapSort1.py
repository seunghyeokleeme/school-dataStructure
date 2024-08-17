from heap import Heap

def heapSort(A):
    B = [x for x in A]
    h = Heap(B)
    h.buildHeap()
    for i in range(len(B)-1, -1, -1):
        A[i] = h.deleteMax()