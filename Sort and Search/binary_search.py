#2017025073 강병욱
#이진탐색
def binary_search(A,key,low,high):
    if(low<=high): #항목들이 남아 있으면(종료조건)
        middle = (low+high)//2 
        if key == A[middle]:    #탐색성공
            return middle
        elif key<A[middle]: #왼쪽 부분리스트 탐색
            return binary_search(A,key,low,middle-1)
        else:               #오른쪽 부분리스트 탐색
            return binary_search(A,key,middle+1,high)
    return None #탐색실패

data=[2,26,11,13,18,20,22,27,29,30,34,38,41,42,45,47]
print("Original :",data)
idx=binary_search(data,22,0,len(data))
print("Find Index",idx)