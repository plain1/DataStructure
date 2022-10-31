import math
(ox,oy) = (5,4)
def dist(x,y):
    (dx,dy)=(ox-x,oy-y)
    return math.sqrt(dx*dx+dy*dy)
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
                if self.items[i][2] > self.items[highest][2]:
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

def isValidPos(x,y):
    if(x<0 or y <0 or x>=MAZE_SIZE or y >= MAZE_SIZE):
        return False
    elif (map[y][x] == '0' or map[y][x] == 'x'):
        return True

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print("PQueue: ")
    
    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2],end='->')
        x,y,_ = here
        if map[y][x] == 'x':
            return True
        else:
            if isValidPos(x,y-1):
                q.enqueue((x,y-1,-dist(x,y-1)))
            if isValidPos(x,y+1):
                q.enqueue((x,y+1,-dist(x,y+1)))
            if isValidPos(x-1,y):
                q.enqueue((x-1,y,-dist(x-1,y)))
            if isValidPos(x+1,y):
                q.enqueue((x+1,y,-dist(x+1,y)))
        print('우선순위큐:',q.items)
    return False
