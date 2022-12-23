MAX_VAL=1000
def counting_sort(A):
    output = [0]*MAX_VAL    #정렬 결과를 저장
    count = [0]*MAX_VAL     #각 숫자의 빈도를 저장

    for i in A:             #각 숫자별 빈도를 계산
        count[i] += 1
    
    for i in range(MAX_VAL):    #count[i]가 출력 배열에서
        count[i] += count[i-1]  #해당 숫자의 위치가 되도록 수정

    for i in range(len(A)):     #정렬된 배열 만들기
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1
    
    for i in range(len(A)):     #정렬 결과를 원래 배열에 복사
        A[i] = output[i]

















