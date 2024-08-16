from circularDoublyLinkedList import *

list = CircularDobulyLinkedList()
list.append(30); list.insert(0, 20)
a = [4, 3, 3, 2, 1]
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()