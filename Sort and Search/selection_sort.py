#2017025073 강병욱
#선택정렬
def selection_sort(A):
    n = len(A)
    for i in range(n-1):    #오른쪽 리스트 최솟값을 선택
        least = i
        for j in range(i+1, n):
            if(A[j]<A[least]):  
                least = j
        A[i],A[least] = A[least],A[i] #왼쪽 리스트의 맨 뒤로 이동
        print('Step',end="")
        print(i+1,end="")
        print('=',end="")
        print(A)

data = [5,3,8,4,9,1,6,2,7]
print("Original :",data)
selection_sort(data)
print("Selection : ",data)