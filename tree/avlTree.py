class AVLNode:
    def __init__(self, newItem, left, right, h):
        self.item = newItem
        self.left = left
        self.right = right
        self.height = h

class AVLTree:
    def __init__(self):
        self.NIL = AVLNode(None, None, None, 0)
        self.__root = self.NIL
        self.LL = 1; self.LR = 2; self.RR = 3; self.RL = 4
        self.NO_NEED = 0
        self.ILLEGAL = -1

    def search(self, x):
        return self.__searchItem(self.__root, x)

    def __searchItem(self, tNode: AVLNode, x) -> AVLNode:
        if tNode == self.NIL:
            return self.NIL
        elif x == tNode.item:
            return tNode
        elif x < tNode.item:
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)
        
    def insert(self, x):
        self.__root = self.__insertItem(self.__root, x)

    def __insertItem(self, tNode: AVLNode, x) -> AVLNode:
        if tNode == self.NIL:
            tNode = AVLNode(x, self.NIL, self.NIL, 1)
        elif x < tNode.item:
            tNode.left = self.__insertItem(tNode.left, x)
            tNode.height = 1 + max(tNode.left.height, tNode.right.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)
        else:
            tNode.right = self.__insertItem(tNode.right, x)
            tNode.height = 1 + max(tNode.left.height, tNode.right.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                tNode = self.__balanceAVL(tNode, type)
        
        return tNode
    
    def delete(self, x):
        self.__root = self.__deleteItem(self.__root, x)

    def __deleteItem(self, tNode:AVLNode, x) -> AVLNode:
        if tNode == self.NIL:
            return self.NIL
        else:
            if x == tNode.item:
                tNode = self.__deleteNode(tNode)
            elif x < tNode.item:
                tNode.left = self.__deleteItem(tNode.left, x)
                tNode.height = 1 + max(tNode.left.height, tNode.right.height)
                type = self.__needBalance(tNode)
                if type != self.NO_NEED:
                    self.__balanceAVL(tNode, type)
            else:
                tNode.right = self.__deleteItem(tNode.right, x)
                tNode.height = 1 + max(tNode.left.height, tNode.right.height)
                type = self.__needBalance(tNode)
                if type != self.NO_NEED:
                    self.__balanceAVL(tNode, type)

        return tNode
    
    def __deleteNode(self, tNode:AVLNode) -> AVLNode:
        if tNode.left == self.NIL and tNode.right == self.NIL:
            return self.NIL
        elif tNode.left == self.NIL:
            return tNode.right
        elif tNode.right == self.NIL:
            return tNode.left
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.right)
            tNode.item = rtnItem
            tNode.right = rtnNode
            tNode.height = 1 + max(tNode.left.height, tNode.right.height)
            type = self.__needBalance(tNode)
            if type != self.NO_NEED:
                self.__balanceAVL(tNode, type)
            return tNode
        
    def __deleteMinItem(self, tNode:AVLNode) -> tuple:
        if tNode.left == self.NIL:
            return (tNode.item, tNode.right)
        else:
            (rtnItem, rtnNode) = self.__deleteMinItem(tNode.left)
            tNode.left = rtnNode
            tNode.height = 1 + max(tNode.left.height, tNode.right.height)
            if type != self.NO_NEED:
                self.__balanceAVL(tNode, type)
            return (rtnItem, tNode)
    

    def __balanceAVL(self, tNode:AVLNode, type:int) -> AVLNode:
        returnNode = self.NIL
        if type == self.LL:
            returnNode = self.__rightRotate(tNode)
        elif type == self.LR:
            tNode.left = self.__leftRotate(tNode.left)
            returnNode = self.__rightRotate(tNode)
        elif type == self.RR:
            returnNode = self.__leftRotate(tNode)
        elif type == self.RL:
            tNode.right = self.__rightRotate(tNode.right)
            returnNode = self.__leftRotate(tNode)
        else:
            print("불가능한 타입입니다! LL, LR, RR, RL 중 하나의 타입만 가질수 있습니다.")
        return returnNode
    
    def __leftRotate(self, t:AVLNode) -> AVLNode:
        RChild = t.right
        if RChild == self.NIL:
            print(t.item, "RChild는 NIL이 될수 없습니다!")
        RLChild = RChild.left
        RChild.left = t
        t.right = RLChild
        t.height = 1 + max(t.left.hight, t.right.height)
        RChild.height = 1 + max(RChild.left.height, RChild.right.height)
        return RChild
    
    def __rightRotate(self, t:AVLNode) -> AVLNode:
        LChild = t.left
        if LChild == self.NIL:
            print(t.item, "LChild는 NIL이 될수 없습니다!")
        LRChild = LChild.right
        LChild.right = t
        t.left = LRChild
        t.height = 1 + max(t.left.hight, t.right.height)
        LChild.height = 1 + max(LChild.left.height, LChild.right.height)
        return LChild
    
    def __needBalance(self, t:AVLNode) -> int:
        type = self.ILLEGAL
        if (t.left.height + 2 <= t.right.height):
            if (t.right.left.height) <= t.right.right.height:
                type = self.RR
            else:
                type = self.RL
        elif (t.left.height) >= t.right.height + 2:
            if (t.left.left.height) >= t.left.right.height:
                type = self.LL
            else:
                type = self.LR
        else:
            type = self.NO_NEED
        
        return type


    def isEmpty(self) -> bool:
        return self.__root == self.NIL
    
    def clear(self):
        self.__root = self.NIL
    

        