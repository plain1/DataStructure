def shell_sort(A):                          #셸 정렬 알고리즘
    n = len(A)                             
    gap = n//2                              #최초의 gap:리스트 크기의 절반
    while gap > 0:
        if(gap%2)==0:
            gap+=1                          #gap이 짝수이면 1을 더함
        for i in range(gap):
            sortGapInsertion(A,i,n-1,gap)
        print('Gap=',gap,A)                 #중간 결과 출력용
        gap = gap//2                        #gap을 반으로 줄임(정수 나눗셈)

def sortGapInsertion(A,first,last,gap):
    for i in range(first+gap,last+1,gap):
        key = A[i]
        j = i - gap
        while j >= first and key < A[j]:    #삽입 위치를 찾음
            A[j+gap]=A[j]                   #항목 이동
            j=j-gap
        A[j+gap]=key                        #최종 위치에 삽입

        

