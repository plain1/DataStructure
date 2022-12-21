vertex = ['A','B','C','D','E','F','G']
weight=[[None, 29, None, None, None, 10, None],
        [29, None, 16, None, None, None, 15],
        [None, 16, None, 12, None, None, None],
        [None, None, 12, None, 22, None, 18],
        [None, None, None, 22, None, 27, 25],
        [10, None, None, None, 27, None, None],
        [None, 15, None, 18, 25, None, None]]
graph = (vertex,weight)

def weightSum(visit,W):                 #매개변수: 정점리스트, 인접행렬
    sum = 0                             #가줃치의 합
    for i in range(len(visit)):         #모든 정점에 대해(i:0,...N-1)
        for j in range(i+1,len(visit)): #하나의 행에 대해(삼각영역)
            if W[i][j] != None :        #만약 간선이 있으면
                sum += W[i][j]          #sum에 추가
    return sum                          #전체 가중치 합을 반환

print('AM: weight =',weightSum(vertex,weight))

def printAllEdges(vlist,W):                                              #매개변수: 정점 리스트, 인접 행렬   
    for i in range(len(vlist)):                                                         
        for j in range(i+1,len(W[i])):                                   #모든 간선 W[i][j]에 대해
            if W[i][j] != None and W[i][j] != 0:                         #간선이 있으면   
                print("(%s,%s,%d)"%(vlist[i],vlist[j],W[i][j]),end='')
    print()

printAllEdges(vertex,weight)    









