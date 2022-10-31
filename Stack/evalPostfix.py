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
        
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if(token == '+'):
                s.push(val1+val2)
            elif(token == '-'):
                s.push(val1-val2)
            elif(token == '*'):
                s.push(val1*val2)
            elif(token == '/'):
                s.push(val1/val2)
        else:
            s.push(float(token))
    return s.pop()