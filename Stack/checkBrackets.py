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

def checkBrackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{','[','('):
            stack.push(ch)
        elif ch in ('}',']',')'):
            if stack.isEmpty():
                return False
            else:
                left = stack.pop()
                if (ch=='}' and left != '{') or (ch==']' and left != "[") or (ch == ")" and left != "("):
                    return False
    return stack.isEmpty()