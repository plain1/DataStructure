class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
        
    def isEmpty(self):
        return self.tail == None
    def clear(self):
        self.tail = None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self,item):
        node = Node(item,None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
            
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count
    def display(self,msg='CircularLinkedQueue:'):
        print(msg,end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data,end=' ')
                node = node.link
            print(node.data, end = ' ')
        print()