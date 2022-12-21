def MSTPrim(vertex,adj):
    vsize = len(vertex)
    dist = [INF]*vsize          #dist: [INF,INF,...INF]
    selected = [False]*vsize    #selected: [False,False,...False]
    dist[0]=0                   #dist : [0,INF,...INF]

    for i in range(vsize):      #정점의 수 만큼 반복
        u = getMinVertex(dist,selected)
        selected[u] = True  #u는 이제 선택됨
        print(vertex[u],end='') #u를 출력
        for v in range(vsize):  #내부 루프
            if(adj[u][v]!=None):#(u,v) 간선이 있으면 dist[v]갱신
                if selected[v]==False and adj[u][v]<dist[v]:
                    dist[v] = adj[u][v]

    print()