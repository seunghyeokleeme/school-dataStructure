class ListQueue:
    def __init__(self):
        self.__queue = []
    
    def enqueue(self, x):
        self.__queue.append(x)

    def dequeue(self):
        return self.__queue.pop(0)

    def front(self):
        if self.isEmpty():
            return None
        else:
            return self.__queue[0]

    def isEmpty(self) -> bool:
        return not bool(self.__queue)
    
    def dequeueAll(self):
        self.__queue.clear()

    def printQueue(self):
        print("Queue from front:", end=' ')
        for i in range(len(self.__queue)):
            print(self.__queue[i], end=' ')
        print()