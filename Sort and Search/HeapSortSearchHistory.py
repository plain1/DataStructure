def MaxHeapify(A,i,size): #Max_Heap의 성질 유지 연산 함수
    largest = i
    l= 2*i+1
    r = 2*i+2
    if l< size and A[l] > A[i]:
        largest = l
    if r < size and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A,largest,size)

def HeapSort(A): #HeapSort 연산 함수
    size = len(A)
    for i in range(size//2-1,-1,-1):
        MaxHeapify(A,i,size)
    for i in range(size-1,0,-1):
        A[0],A[i] = A[i],A[0]
        MaxHeapify(A,0,i)
    return A

num = int(input()) #입력값들 개수
history = {} 
A=[]
for i in range(num):
    year,event = input().split() #년도, 사건 입력
    year = int(year)
    A.append(year) #년도를 list로 저장
    history[year] = event  #년도와 사건을 dictionary로 저장
print()
HeapSort(A)
for i in range(num):
    print(A[i],history[A[i]]) #출력