#2017025073 강병욱
#순차탐색

def sequential_search(A,key,low,high): #순차탐색
    for i in range(low,high+1):
        if A[i] == key: #탐색 성공하면
            return i #인덱스 반환
    return None #탐색에 실패하면 None 반환

data = [9,5,8,3,7]
print("Original :",data)
idx=sequential_search(data,8,0,4)
print("Find Index",idx)