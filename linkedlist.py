class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val=None
        self.next=None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if self.val==None:
            return -1
        x=self
        y=0
        while x!=None:
            if y==index:
                return x.val
            x=x.next
            y+=1   
        return -1    

    def addAtHead(self, val:int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        if self.val==None:
            self.val=val
        else:
            x=self.val
            z=self.next
            self.val=val
            self.next=MyLinkedList()
            self.next.val=x
            self.next.next=z
        

    def addAtTail(self, val:int)->None:
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.val==None:
            self.val=val
        elif self.val!=None:
            x=self
            y=0
            while x.next!=None:
                x=x.next
                y+=1
            x.next=MyLinkedList()
            x.next.val=val

    def addAtIndex(self, index, val: int)-> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        y=0
        i=0
        x=self
        z=x
        index=index-1
        while y<index:
            y+=1
            if x.next!=None:
                x=x.next
                z=x
            else:
                i+=1
        if index<=-1:
            self.addAtHead(val)
        elif i==0 and x.next!=None:
            z=x.next
            x.next=MyLinkedList()
            x.next.val=val
            x.next.next=z
        elif i<=1 and x.val!=None:
            self.addAtTail(val)

    def deleteAtIndex(self, index: int)->None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        y=0
        x=self
        z=x
        i=0
        while y<index:
            y+=1
            if x.next!=None:
                z=x
                x=x.next
            else:
                i+=1
        if index==0 and x.next==None:
            x.val=None
        elif index>=0 and i==0 and x.next!=None:
            x.val=x.next.val
            x.next=x.next.next
        elif index>0 and i==0 and x.val!=None:
            z.next=None
        else:
            return
