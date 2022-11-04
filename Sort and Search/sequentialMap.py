#2017025073 강병욱
#리스트를 이용한 순차탐색 맵
class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))


class SequentialMap:        #순차탐색 맵
    def __init__(self):
        self.table=[]       #맵의 레코드 테이블
    def insert(self,key,value): #삽입연산
        self.table.append(Entry(key,value)) #리스트의 맨 뒤에 추가
    
    def sequential_search(self,key,low,high):   #순차탐색
        for i in range(low,high+1):
            if self.table[i] == key:
                return i
        return None
    
    def size(self): #리스트의 크기
        return len(self.table)

    def search(self,key):   #순차탐색연산
        pos = self.sequential_search(key,0,self.size()-1)
        if pos is not None:
            return self.table[pos]
        else:
            return None

    def delete(self,key):   #삭제연산 : 항목 위치를 찾아 pop
        for i in range(self.size()):
            if self.table[i].key == key:    #삭제할 위치를 먼저 찾고
                return self.table.pop(i)    #리스트의 pop으로 삭제

    def display(self,string): #리스트 표시
        print(string)
        for i in self.table:
            print(i)

map = SequentialMap()
map.insert('data','자료')
map.insert('structure','구조')
map.insert('sequential search','선형탐색')
map.insert('game','게임')
map.insert('binary search','이진탐색')
map.display("나의 단어장:")

print("탐색:game -->",map.search('game'))
print("탐색:over -->",map.search('over'))
print("탐색:data -->",map.search('data'))

map.delete('game')
map.display('나의 단어장: ')