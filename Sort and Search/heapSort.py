from heapify import *

def heapSort(arr):                  
    n = len(arr)                    
    print("i=",0,arr)   #중간결과 출력용
    for i in range(n//2,-1,-1): #최대 힙을 만듦: i: n//2,...,1,0
        heapify(arr,n,i)    #heap 조건을 맞춤(downheap)
        print("i=",i,arr)   #중간결과 출력용
    print()

    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i] #루트를 뒤쪽으로 옮김, 교체
        heapify(arr,i,0)    #heap 조건을 맞춤(downheap)
        print("i=",i,arr)   #중간결과 출력용