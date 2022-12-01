#깊이 우선 탐색
def defs(graph, start, visited = set()): #처음 호출할 때 visited 공집합
    if start not in visited :           #start가 방문하지 않은 정점이면
        visited.add(start)              #start를 방문한 노드 집합에 추가
        print(start,end='')             #start를 방문했다고 출력
        nbr = graph[start]-visited      #nbr: 차집합 연산 이용
        for v in nbr:                   #v는 {인접정점}-{방문정점}에 포함
            defs(graph,v,visited)        #v에 대해 dfs를 순환적으로 호출