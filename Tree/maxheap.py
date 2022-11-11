#2017025073 강병욱
#최대힙
class MaxHeap:                                 #최대힙 클래스   
    def __init__(self):                        #생성자
        self.heap = []                         #리스트를 이용한 힙
        self.heap.append(0)                    #0번 항목은 사용하지 않음


    def size(self):                            #힙의 크기
        return len(self.heap)-1                 
    
    def isEmpty(self):                         #공백검사
        return self.size()==0
    
    def Parent(self,i):                        #부모노드 반환
        return self.heap[i//2]

    def Left(self,i):                          #왼쪽 서브트리 반환
        return self.heap[i*2]

    def Right(self,i):                         #오른쪽 서브트리 반환
        return self.heap[i*2+1]

    def display(self,msg='힙 트리'):
        print(msg,self.heap[1:])               #리스트 슬라이싱

    def insert(self, n):
        self.heap.append(n)                    #맨 마지막 노드로 일단 삽입
        i = self.size()                        #노드 n의 위치
        while(i != 1 and n > self.Parent(i)):  #부모보다 큰 동안 계속 업힘
            self.heap[i] = self.Parent(i)      #부모를 끌어내림
            i = i // 2                         #i를 부모의 인덱스로 올림
        self.heap[i] = n                       #마지막 위치에 n 삽입
    
    def delete(self):                       
        parent = 1
        child = 2
        if not self.isEmpty():
            hroot = self.heap[1]                #삭제할 루트를 복사해 둠
            last = self.heap[self.size()]       #마지막 노드
            while(child <= self.size()):        #마지막 노드 이전까지
                if child < self.size() and self.Left(parent)<self.Right(parent):
                    child+=1
                if last >= self.heap[child]:    #더 큰 자식이 더 작으면
                    break                       #삽입 위치를 찾음. down-heap종료
                self.heap[parent] = self.heap[child] #아니면 down-heap적용
                parent = child
                child *= 2

        self.heap[parent] = last    #맨 마지막 노드를 parent위치에 복사
        self.heap.pop(-1)           #맨 마지막 노드 삭제
        return hroot                #저장해두었던 루트를 반환

heap = MaxHeap()                    #Maxheap 객체 생성
data = [2,5,4,8,9,3,7,3]            #힙에 삽입할 데이터
print("[삽입연산] : "+str(data))   
for elem in data:       
    heap.insert(elem)
heap.display('[삽입후]:')
heap.delete()
heap.display('[삭제후]:')
heap.delete()
heap.display('[삭제후]:')