from bidrectNode import BidirectNode

class CircularDobulyLinkedList:
    def __init__(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def insert(self, i: int, newItem) -> None:
        if (i>= 0 and i <= self.__numItems):
            prev = self.getNode(i-1)
            newNode = BidirectNode(newItem, prev, prev.next)
            newNode.next.prev = newNode
            prev.next = newNode
            self.__numItems += 1
        else:
            print("index", i, ": out of bound in insert()")

    def append(self, newItem) -> None:
        prev = self.__head.prev
        newNode = BidirectNode(newItem, prev, self.__head)
        prev.next = newNode
        self.__head.prev = newNode
        self.__numItems += 1

    def pop(self, *args):
        if self.isEmpty():
            return None
        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        if(i >= 0 and i <= self.__numItems -1):
            curr = self.getNode(i)
            retItem = curr.item
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return retItem
        else:
            return None

    def remove(self, x):
        curr = self.__findNode(x)
        if curr != None:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            self.__numItems -= 1
            return x
        else:
            return None
        
    def get(self, *args):
        if self.isEmpty(): return None

        if len(args) != 0:
            i = args[0]
        if len(args) == 0 or i == -1:
            i = self.__numItems -1
        
        if(i >= 0 and i <= self.__numItems-1):
            return self.getNode(i).item
        else:
            return None
        
    def index(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                return cnt
            cnt += 1
        return -12345
        
    def isEmpty(self) -> bool:
        return self.__numItems == 0
    
    def size(self) -> int:
        return self.__numItems

    def clear(self):
        self.__head = BidirectNode("dummy", None, None)
        self.__head.prev = self.__head
        self.__head.next = self.__head
        self.__numItems = 0

    def count(self, x) -> int:
        cnt = 0
        for element in self:
            if element == x:
                cnt += 1
        return cnt
    
    def extend(self, a) -> None:
        for element in a:
            self.append(element)

    def copy(self) -> 'CircularDobulyLinkedList':
        a = CircularDobulyLinkedList()
        for element in self:
            a.append(element)
        return a
    
    def reverse(self) -> None:
        prev = self.__head; curr = prev.next; next = curr.next
        self.__head.next = prev.prev; self.__head.prev = curr
        for i in range(self.__numItems):
            curr.next = prev; curr.prev = next
            prev = curr; curr = next; next = next.next

    def sort(self) -> None:
        a = []
        for element in self:
            a.append(element)
        a.sort()
        pass

    def __findNode(self, x) -> BidirectNode:
        curr = self.__head.next
        while curr != self.__head:
            if curr.item == x:
                return curr
            else:
                curr = curr.next
        return None

    def getNode(self, i:int) -> BidirectNode:
        curr = self.__head
        for index in range(i+1):
            curr = curr.next
        return curr
    
    def printList(self) -> None:
        for element in self:
            print(element, end=" ")
        print()
    
    def __iter__(self):
        return CircularDobulyLinkedListIterator(self)

class CircularDobulyLinkedListIterator:
    def __init__(self, alist):
        self.__head = alist.getNode(-1)
        self.iterPosition = self.__head.next
    
    def __next__(self):
        if self.iterPosition == self.__head:
            raise StopIteration
        else:
            item = self.iterPosition.item
            self.iterPosition = self.iterPosition.next
            return item