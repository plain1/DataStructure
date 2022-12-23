class MaxPriorityQueue: #Max-Priority-Queue 연산 클래스
    def __init__(self): #생성자
        self.top = []
    
    def Maximum(self): #최대값 원소 반환
        return self.top[0]
    
    def MaxHeapify(self,i,size): #Max-Heap연산
        largest = i
        l= 2*i+1
        r = 2*i+2
        if l< size and self.top[l] > self.top[i]:
            largest = l
        if r < size and self.top[r] > self.top[largest]:
            largest = r
        if largest != i:
            self.top[i], self.top[largest] = self.top[largest], self.top[i]
            self.MaxHeapify(largest,size)
            
    def ExtractMax(self): #최대값 원소 반환 및 제거
        size = len(self.top)
        if size < 1:
            print("heap underflow")
        Max = self.top[0]
        self.top[0] = self.top[size-1]
        self.top.pop(size-1)
        size-=1
        self.MaxHeapify(0,size)
        return Max
    
    def IncreaseKey(self,i,key): #키값 증가
        self.top[i] = key
        while i>0 and self.top[i//2] < self.top[i]:
            self.top[i//2], self.top[i] = self.top[i], self.top[i//2]
            i = i//2
    
    def Insert(self,key): #삽입
        size = len(self.top)
        self.top.append(0)
        self.IncreaseKey(size,key) 
    
num = int(input()) #입력값 개수 입력
history = {}
queue = MaxPriorityQueue() #클래스 지정
for i in range(num): 
    year,event = input().split() #년도, 사건 입력
    year = int(year)
    queue.Insert(year) #년도 큐에 삽입
    history[year] = event  #년도, 사건 dictionary로 저장
print()
for i in range(num): 
    print(queue.Maximum(),history[queue.Maximum()]) #출력
    queue.ExtractMax()