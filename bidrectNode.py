class BidirectNode:
    def __init__(self, x, prevNode: 'BidirectNode', nextNode: 'BidirectNode'):
        self.item = x
        self.prev = prevNode
        self.next = nextNode