#2017025073 강병욱
#이진탐색트리
class BSTNode:                          #이진탐색트리를 위한 노드 클래스
    def __init__(self,key,value):       #생성자: 키와 값을 받음
        self.key = key                  #키
        self.value = value              #값
        self.left = None                #왼쪽 자식에 대한 링크
        self.right = None               #오른쪽 자식에 대한 링크

def search_bst(n,key):                  #이진탐색트리 탐색연산(순환함수)
    if n == None:
        return None
    elif key == n.key:
        return n
    elif key < n.key:
        return search_bst(n.left,key)
    else:
        return search_bst(n.right,key)

def search_bst_iter(n,key):             #이진탐색트리 탐색연산(반복함수)
    while n != None:                    
        if key == n.key:
            return n
        elif key < n.key:
            n=n.left
        else:
            n=n.right
    return None

def search_max_bst(n):                   #최대 값의 노드 탐색
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):                   #최소 값의 노드 탐색
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r,n):                   #이진탐색트리 삽입연산 (노드를 삽입함): 순환구조 이용
    if n.key < r.key:                  #삽입할 노드의 키가 루트보다 작으면
        if r.left is None:             #루트의 왼쪽 자식이 없으면
            r.left = n                  #n은 루트의 왼쪽 자식이 됨
            return True
        else:                           #루트의 왼쪽 자식이 있으면
            return insert_bst(r.left,n) #왼쪽 자식에게 삽입하도록 함
    elif n.key > r.key:                 #삽입할 노드의 키가 루트보다 크면
        if r.right is None:             #루트의 오른쪽 자식이 없으면
            r.right = n                 #n은 루트의 오른쪽 자식이 됨
            return True
        else:                           #루트의 오른쪽 자식이 있으면
            return insert_bst(r.right,n) #오른쪽 자식에게 삽입하도록 함
    else:                               # 키가 중복되면
        return False                    #삽입하지 않음

def delete_bst_case1(parent,node,root): 
    if parent is None:                  #삭제할 단말 노드가 루트이면
        root = None                     #공백 트리가 됨
    else:
        if parent.left == node:         #삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None          #부모의 왼쪽 링크를 None
        else:                           #오른쪽 자식이면
            parent.right = None         #부모의 오른쪽 링크를 None
        
    return root                         #root가 변경될 수도 있으므로 반환

def delete_bst_case2(parent,node,root):
    if node.left is not None:          
        child = node.left
    else:
        child = node.right
    if node == root:
        root = child
    else:
        if node is parent.left:
            parent.left =child
        else:
            parent.right = child
    return root

def delete_bst_case3(parent,node,root):
    succp = node                            #후계자의 부모노드
    succ = node.right                       #후계자 노드
    while(succ.left != None):               #후계와 부모노드 탐색
        succp = succ            
        succ = succ.left

    if (succp.left == succ):            #후계자가 왼쪽 자식이면
        succp.left =succ.right          #후계자의 오른쪽 자식 연결
    else:                               #후계자가 오른쪽 자식이면
        succp.right = succ.right        #후계자의 왼쪽 자식 연결
    node.key = succ.key                 #후계자의 키와 값을
    node.value = succ.value             #삭제할 노드에 복사
    node = succ                         #실제로 삭제하는 것은 후계자 노드
    return root                         #일관성을 위해 root반환

def delete_bst(root,key):               #이진탐색트리 삭제연산(노드를 삭제함)
    if root == None:                    
        return None                     #공백트리
    parent = None                       #삭제할 노드의 부모탐색
    node = root                         #삭제할 노드 탐색
    while node != None and node.key != key:     #parent 탐색
        parent = node
        if key < node.key:
            node = node.left
        else:
            node = node.right

    if node == None:                                #삭제할 노드가 없음
        return None             
    if node.left == None and node.right == None:    #case1:단말노드
        root = delete_bst_case1(parent,node,root)   
    elif node.left ==None or node.right == None:    #case2:유일한 자식
        root = delete_bst_case2(parent,node,root)
    else:                                           #case3:두 개의 자식
        root = delete_bst_case3(parent,node,root)
    return root                                     #변경된 루트 노드를 반환

def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.key, end=' ')
        inorder(n.right)

class BSTMap():                             #이진탐색트리르 이용한 맵
    def __init__(self):                     #생성자
        self.root = None                    #트리의 루트 노드
    def isEmpty(self):                      #맵 공백검사
        return self.root == None
    def clear(self):                        #맵 초기화
        self.root = None
    def size(self):                         #레코드(노드) 수 계산
        return count_node(self.root)

    def search(self,key):
        return search_bst(self.root, key)
    
    def searchValue(self,key):
        return search_value_bst(self.root ,key)
    
    def findMax(self):
        return search_max_bst(self.root)

    def findMin(self):
        return search_min_bst(self.root)

    def insert(self,key,value=None):        #삽입연산
        n = BSTNode(key,value)              #키와 값으로 새로운 노드 생성
        if self.isEmpty():                  #공백이면
            self.root = n                   #루트노드로 삽입
        else:                               #공백이 아니면
            insert_bst(self.root,n)         #insert_bst() 호출
    def delete(self,key):                   #삭제 연산
        self.root = delete_bst(self.root,key)   #delete_bst()호출
    def display(self,msg='BSTMap:'):
        print(msg,end=" ")
        inorder(self.root)
        print()

map = BSTMap()
data = [35,18,7,26,12,3,68,22,30,99]

print("[삽입연산] : ",data)
for key in data:
    map.insert(key)             #삽입 연산 테스트

map.display("[중위순회] : ")    #삽입 결과 출력: 중위순회
if map.search(26) != None :     #탐색연산 테스트
    print('[탐색 26 ]:성공')
else:
    print('[탐색 26 ]:실패')
if map.search(25) != None :     #탐색연산 테스트
    print('[탐색 25 ]:성공')
else:
    print('[탐색 25 ]:실패')

map.delete(3)                   #삭제연산 테스트
map.display('[ 3삭제]:')
map.delete(68)
map.display('[ 68삭제]:')
map.delete(18)
map.display('[ 18삭제]:')
map.delete(35)
map.display('[ 35삭제]:')