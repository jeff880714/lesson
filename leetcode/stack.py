class Node:
    def __init__(self, val, nextNode=None):
        self.val = val
        self.min = val
        self.next = nextNode
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.topNode=None

    def push(self, x: int) -> None:
        if self.topNode is None:
            self.topNode=Node(x,None)
        else:
            y=self.topNode.min
            self.topNode=Node(x,self.topNode)
            if y<self.topNode.val:
                self.topNode.min=y
                
    def pop(self) -> None:
        self.topNode=self.topNode.next

    def top(self) -> int:
        return self.topNode.val

    def getMin(self) -> int:
        return self.topNode.min
