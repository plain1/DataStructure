#2017025073 강병욱
#체이닝을 이용한 해시 맵
class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))

class Node:
    def __init__(self,elem,link=None):
        self.data=elem
        self.link=link

class HashChainMap:
    def __init__(self,M):
        self.table =[None]*M
        self.M=M
    
    def hashFn(self,key):
        sum = 0
        for c in key:
            sum+=ord(c)
        return sum%self.M

    def insert(self,key,value): #(key,value) 입력
        idx = self.hashFn(key)  #해시 주소 계산
        self.table[idx] = Node(Entry(key,value),self.table[idx])    #전단 삽입
        entry = Entry(key,value)    #엔트리를 생성
        node = Node(entry)          #엔트리로 노드를 생성
        node.link = self.table[idx] #노드의 링크필드 처리
        self.table[idx] = node      #테이블의 idx항목: node로 시작
    
    def search(self,key):
        idx=self.hashFn(key)
        node= self.table[idx]
        while node is not None:
            if node.data.key == key:
                return node.data
            node = node.link
        return None
    
    def delete(self,key):
        idx=self.hashFn(key)
        node=self.table[idx]
        before = None
        while node is not None:
            if node.data.key == key:
                if before == None:
                    self.table[idx] = node.link
                else:
                    before.link = node.link
                return 
            before= node
            node = node.link

    def display(self,msg):
        print(msg)
        for idx in range(len(self.table)):
            node = self.table[idx]
            if node is not None:
                print("[%2d] ->"%idx,end="")
                while node is not None:
                    print(node.data,end='->')
                    node=node.link
                print()

map = HashChainMap(10)
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential search','선형탐색')
map.insert('game','게임')
map.insert('binary search','이진탐색')
map.display("나의 단어장:")

print("탐색:game -->",map.search('game'))
print("탐색:over -->",map.search('None'))
print("탐색:data -->",map.search('data'))

map.delete('game')
map.display('나의 단어장: ')
