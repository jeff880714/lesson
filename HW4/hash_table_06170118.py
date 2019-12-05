from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):
        i = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        index = i%self.capacity
        node = self.data[index]
        if self.data[index] == None:
            self.data[index] = ListNode(i)
        else:
            if self.val[index] !=None:              
                while node.next.i != i:
                    node = node.next
                if node.next == None:
                    node.next = ListNode(i)
            else:
                return False
    def remove(self, key):
        if self.contains(key) == False:
            return
        else:
            i = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
            index = i%self.capacity
            node = self.data[index]
            if node.val == i:
                if node.next is True:
                    self.data[index] = node.next
                else:
                    self.data[index] = None
            else:
                while node.next.val != i:
                    node = node.next
    def contains(self, key):
        i = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        index = i%self.capacity
        node = self.data[index]
        while node:
            if node.val == i:
                return True
            node =node.next
        return False
#參考資料:https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
#        https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
