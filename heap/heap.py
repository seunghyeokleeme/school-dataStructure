class Heap:
    def __init__(self, *args):
        if len(args) != 0:
            self.__A = args[0]
        else:
            self.__A = []
    
    def insert(self, x):
        self.__A.append(x)
        self.percolateUp(len(self.__A)-1)
    
    def deleteMax(self):
        if(not self.isEmpty()):
            max = self.__A[0]
            self.__A[0] = self.__A.pop()
            self.percolateDown(0)
            return max
        else:
            return None

    def percolateUp(self, i:int):
        parent = (i - 1) // 2
        if i > 0 and self.__A[i] > self.__A[parent]:
            self.__A[i], self.__A[parent] = self.__A[parent], self.__A[i]
            self.percolateUp(parent)

    def percolateDown(self, i:int):
        child = 2 * i + 1
        right = 2 * i + 2
        if child <= len(self.__A) -1:
            if right <= len(self.__A) -1 and self.__A[child] < self.__A[right]:
                child = right
            if self.__A[i] < self.__A[child]:
                self.__A[i], self.__A[child] = self.__A[child], self.__A[i]
                self.percolateDown(child)


    def max(self):
        return self.__A[0]

    def buildHeap(self):
        for i in range((len(self.__A) -2) // 2, -1, -1):
            self.percolateDown(i)


    def size(self) -> int:
        return len(self.__A)

    def isEmpty(self) -> bool:
        return not bool(self.__A)

    def clear(self):
        self.__A = []

    def printHeap(self):
        print("Heap from index:", end=' ')
        for i in range(len(self.__A)):
            print(self.__A[i], end=' ')
        print()