def shortest_path_floyd(vertex,adj):  #Floyd의 최단경로탐색 함수
    vsize = len(vertex)               #정점의 개수
    A = list(adj)                     #주의: 2차원 배열(리스트의 리스트)의 복사  
    for i in range(vsize):            #각각의 열에 대해  
        A[i] = list(adj[i])           #열(리스트)을 복사

    for k in range(vsize):            #정점 k를 추가할 떼  
        for i in range(vsize):          
            for j in range(vsize):    #모든 A[i][j] 갱신  
                if(A[i][k] + A[k][j] < A[i][j]):
                    A[i][j] = A[i][k] + A[k][j]

        print(A)            #현재 A 행렬 출력