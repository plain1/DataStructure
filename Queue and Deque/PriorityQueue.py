class PriorityQueue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]
    def enqueue(self,item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1,self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
        
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
        
    def peek(self):
        highest = findMaxIndex()
        if highest is not None:
            return self.items[highest]