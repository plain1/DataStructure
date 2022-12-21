def shortest_path_dijkstra(vtx,adj,start):
    vsize = len(vtx)                    #정점 수
    dist = list(adj[start])             #dist 배열 생성 및 초기화    
    path = [start]*vsize                #path 배열 생성 및 초기화
    found = [False]*vsize               #found 배열 생성 및 초기화
    found[start]=True                   #시작정점: 이미 찾아짐
    dist[start]=0                       #시작정점의 거리 0

    for i in range(vsize):              
        print("Step%2d:"%(i+1),dist)    #단계별 dist[] 출력용
        u = choose_vertex(dist,found)   #최소 dist 정점 u 탐색
        found[u] = True                 #u는 이제 찾아짐

        for w in range(vsize):          #모든 정점에 대해
            if not found[w]:            #아직 찾아지지 않았으면
                if dist[u] + adj[u][w] < dist[w]: #갱신 조건 검사
                    dist[w] = dist[u] + adj[u][w] #dist 갱신
                    path[w] = u #이전 정점 갱신

    return path #찾아진 최단 경로 반환

print("Shortest Path By Dijkstra Algorithm")
start = 0
vertex=['A','B','C','D','E','F','G']
weight = [[None, 7, None, None, 3, 10, None],
          [7, None, 4, 2, 2, 6, None],
          [None, 4,None,2,None,None,None],
          [None,None,2,None,11,9,4],
          [3,2,None,11,None,None,5],
          [10,6,None,9,None,None,None],
          [None,None,None,4,5,None,None]]
path = shortest_path_dijkstra(vertex, weight, start)



for end in range(len(vertex)):
    if end != start:
        print("[최단경로:%s->%s]%s"%(vertex[start],vertex[end],vertex[end]),end="")
        while(path[end] != start):
            print("<-%s"%vertex[path[end]],end="")
            end = path[end]
        print("<-%s"%vertex[path[end]])
