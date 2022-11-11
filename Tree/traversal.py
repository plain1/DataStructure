#2017025073 강병욱
#순회
MAX_QSIZE = 100
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE
    def isEmpty(self):
        return self.front == self.rear
    def isFull(self):
        return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self):
        self.front = self.rear
    def enqueue(self,item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE)%MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE]\
            +self.items[0:self.rear+1]
        print("[f=%s,r=%d]==>"%(self.front,self.rear),out)

class TNode:
    def __init__(self,data,left,right):
        self.data = data
        self.left = left
        self.right = right

def preorder(n):               #전위 순회 함수  
    if n is not None:          
        print(n.data,end="")   #먼저 루트노드 처리(화면출력)
        preorder(n.left)  #왼쪽 서브트리 처리
        preorder(n.right) #오른쪽 서브트리 처리
    
def inorder(n): #중위 순회 함수
    if n is not None: 
        inorder(n.left)  #왼쪽 서브트리 처리
        print(n.data,end="")  #루트노드 처리(화면출력)
        inorder(n.right) #오른쪽 서브트리 처리
    
def postorder(n): #후위 순회 함수
    if n is not None:
        postorder(n.left) #왼쪽 서브트리 처리
        postorder(n.right) #오른쪽 서브트리 처리
        print(n.data,end="") #루트노드 처리(화면출력)

def levelorder(root):
        queue = CircularQueue() #큐 객체 초기화
        queue.enqueue(root)     #최초에 큐에는 루트 노드만 들어있음.
        while not queue.isEmpty(): #큐가 공백상태가 아닌 동안,
            n = queue.dequeue() #큐에서 맨 앞의 노드 n을 꺼냄
            if n is not None:
                print(n.data,end="") #먼저 노드의 정보를 출력
                queue.enqueue(n.left) #n의 왼쪽 자식 노드를 큐에 삽입
                queue.enqueue(n.right) #n의 오른쪽 자식 노드를 큐에 삽입

def count_node(n):   #순환을 이용해 트리의 노드 수를 계산하는 함수
        if n is None:    #n이 None이면 공백 트리 --> 0을 반환
            return 0
        else:               #좌우 서브트리의 노드수의 합 +1을 반환 (순환이용)
            return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
        if n is None:    #공백트리 --> 0을 반환
            return 0
        elif n.left is None and n.right is None:  #단말노드 --> 1을 반환
            return 1
        else:       #비단말 노드: 좌우 서브트리의 결과 합을 반환
            return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
        if n is None:   #공백트리 --> 0을 반환
            return 0
        hLeft = calc_height(n.left) #왼쪽 트리의 높이 --> hLeft
        hRight = calc_height(n.right) #오른쪽 트리의 높이 --> hRight
        if (hLeft>hRight):      #더 높은 높이에 1을 더해 반환
            return hLeft +1 
        else:
            return hRight + 1

d = TNode('D',None,None)
e = TNode('E',None,None)
b = TNode('B',d,e)
f = TNode('F',None,None)
c = TNode('C',f,None)
root = TNode('A',b,c)

print('\n In-Order:',end='')
inorder(root)
print('\n Pre-Order:',end='')
preorder(root)
print('\n Post-Order:',end='')
postorder(root)
print('\n Level-Order:',end='')
levelorder(root)
print()

print("노드의 개수 = %d개"%count_node(root))
print("단말의 개수 = %d개"%count_leaf(root))
print("트리의 높이 = %d"%calc_height(root))