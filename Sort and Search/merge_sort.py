def merge_sort(A,left,right):
    if left < right:
        mid = (left + right)//2
        merge_sort(A,left,mid)
        merge_sort(A,mid+1,right)
        merge(A, left, mid, right)

def merge(A,left,mid,right):
    global sorted   #병합을 위한 추가적인 배열
    k = left        #배열 C(정렬될 리스트)의 인덱스
    i = left        #배열 A의 인덱스
    j = mid + 1     #배열 B의 인덱스
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i,k = i+1, k+1
        else:
            sorted[k] = A[j]
            j,k = j+1, k+1

    if i > mid:     #한쪽에 남아 있는 레코드의 일괄 복사
        sorted[k:k+right-j+1] = A[j:right+1]    #리스트의 슬라이싱 이용
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]    #리스트의 슬라이싱 이용
    A[left:right+1] = sorted[left:right+1]  #sorted를 원래 배열 A에 복사


