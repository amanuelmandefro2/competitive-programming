class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.length = 0
        self.head = self.tail = None
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.tail.next = self.head 
        self.length += 1
        return True            
        

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
        self.length -= 1  
        return True  
        

    def Front(self) -> int:
        if self.head:
            return self.head.val
        return -1    
        

    def Rear(self) -> int:
        if self.tail:
            return self.tail.val
        return -1    

    def isEmpty(self) -> bool:
        return self.length == 0
        

    def isFull(self) -> bool:
        return self.length == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()