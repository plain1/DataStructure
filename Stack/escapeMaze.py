class Stack:
    def __init__(self):
        self.top = []
    """def __str__(self):
        return str(self.top[::-1])"""
    def isEmpty(self):
        return len(self.top)==0
    def size(self):
        return len(self.top)
    def clear(self):
        self.top =[]
    def push(self,item):
        self.top.append(item)
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def isValidPos(x,y):

    if(x<0 or y <0 or x>=MAZE_SIZE or y >= MAZE_SIZE):
        return False
    elif (map[y][x] == '0' or map[y][x] == 'x'):
        return True

def DFS():
    stack = Stack()
    stack.push((0,1))
    print('DFS:')
    
    while not stack.isEmpty():
        here = stack.pop()
        print(here,end='->')
        (x,y) = here
        if(map[y][x] == 'x'):
            return True
        else:
            map[y][x]='.'
            if isValidPos(x,y-1):
                stack.push((x,y-1))
            if isValidPos(x,y+1):
                stack.push((x,y+1))
            if isValidPos(x-1,y):
                stack.push((x-1,y))
            if isValidPos(x+1,y):
                stack.push((x+1,y))
        print('현재스택:',stack.top)
    return False
