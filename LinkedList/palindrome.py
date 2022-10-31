class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top == None
    def clear(self):
        self.top = None
    def push(self,item):
        n = Node(item,self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count+=1
        return count


def palindrome():
    string = input().lower()
    arr = list(filter(str.isalpha,string))
    stack = LinkedStack()
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