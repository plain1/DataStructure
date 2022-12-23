def radix_sort(A):
    queues = [] #큐의 리스트
    for i in range(BUCKETS):
        queues.append(Queue()) #BUCKETS개의 큐 사용

    n = len(A)
    factor = 1  #1의 자리부터 시작
    for d in range(DIGITS): #모든 자리에 대해
        for i in range(n):  #자릿수에 따라 큐에 삽입
            queues[(A[i]//factor)%10].put(A[i]) #숫자를 삽입
        i = 0
        for b in range(BUCKETS):    #버킷에서 꺼내어 원래의 리스트로
            while not queues[b].empty():    #b번째 큐가 비어있지 않는 동안.
                A[i] = queues[b].get()      #원소를 꺼내 리스트에 저장
                i += 1
        factor *= 10        #그 다음 자리수로 간다.
        print("step",d+1,A) #중간 과정 출력용 문장

import random
BUCKETS = 10
DIGITS = 4
data = []
for i in range(10):
    data.append(random.randint(1,9999)) #1~9999사이의 숫자 10개 생성
radix_sort(data)                        #기수 정렬
print("Radix:",data)                    #결과 출력