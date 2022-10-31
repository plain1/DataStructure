class Stack:
    def __init__(self):
        self.top = []
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
        
def palindrome():
    string = input().lower()
    arr = list(filter(str.isalpha,string))
    stack = Stack()
    for i in range(len(arr)):
        stack.push(arr[i])
    i = 0
    while 1:
        if stack.pop() == arr[i]:  
            i+=1
            if i == int(len(arr)/2):
                print("회문입니다.")
                break
        else: 
            print("회문이 아닙니다.")
            break