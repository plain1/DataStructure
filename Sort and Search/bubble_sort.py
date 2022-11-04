#2017025073 강병욱
#버블정렬
def bubble_sort(A):
    n = len(A)
    for i in range(n-1,0,-1): #인접한 2개 레코드를 비교 후 서로 교환
        bChanged = False #오름차순 확인
        for j in range(i):
            if (A[j]>A[j+1]): 
                A[j],A[j+1] = A[j+1],A[j]
                bChanged = True
        if not bChanged: 
            break
        print('Step',end="")
        print(n-i,end="")
        print('=',end="")
        print(A)

data = [5,3,8,4,9,1,6,2,7]
print("Original :",data)
bubble_sort(data)
print("Selection : ",data)      