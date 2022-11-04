#2017025073 강병욱
#삽입정렬
def insertion_sort(A): 
    n = len(A)
    for i in range(1,n):    #key값에 처음에 비교하려는 값을 대입
        key = A[i]
        j=i-1
        while j>=0 and A[j]>key: #차례대로 비교하고 값을 바꿈
            A[j+1]=A[j] 
            j-=1
        A[j+1] = key
        print('Step',end="")
        print(i+1,end="")
        print('=',end="")
        print(A)

data = [5,3,8,4,9,1,6,2,7]
print("Original :",data)
insertion_sort(data)
print("Selection : ",data)

    