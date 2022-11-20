#2017025073 강병욱
#AVL트리
from binarySearchTree import *
MAX_QSIZE = 10
class CircularQueue:                   #원형큐         
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

def rotateLL(A):
    B = A.left          #시계방향 회전
    A.left = B.right
    B.right = A
    return B            #새로운 루트 B를 반환

def rotateRR(A):
    B= A.right          #반 시계방향 회전
    A.right = B.left
    B.left = A
    return B            #새로운 루트 B를 반환

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)   #LL회전
    return rotateRR(A)      #RR회전

def rotateLR(A):            
    B = A.left
    A.left = rotateRR(B)    #RR회전
    return rotateLL(A)      #LL회전

def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right)<0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

def insert_avl(parent,node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left,node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right,node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러 ")
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.key ,end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

def search_bst(n,key):
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left,key)
    else:
        return search_bst(n.right,key)

def search_bst_iter(n,key):
    while n != None:
        if key == n.key:
            return n
        elif key < n.key:
            n=n.left
        else:
            n=n.right
    return None

def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n



class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()
    def isEmpty(self):
        return self.root == None
    def insert(self,key,value=None):
        n = BSTNode(key,value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root,n)
    def display(self,msg='AVLMap :'):
        print(msg,end=" ")
        levelorder(self.root)
        print()

node = [7,8,9,2,1,5,3,6,4]
map = AVLMap()

for i in node:
    map.insert(i)
    map.display("AVL(%d): "%i)

print("노드의 개수 = %d"%count_node(map.root))
print("단말의 개수 = %d" %count_leaf(map.root))
print("트리의 높이 = %d"%calc_height(map.root))