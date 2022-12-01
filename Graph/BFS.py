#너비 우선 탐색
import collections
def bfs(graph,start):                  
    visited = set([start])              #맨 처음에는 start만 방문한 정점임
    queue = collections.deque([start])  #컬렉션의 덱 객체 생성(큐로 사용)
    while queue:                        #공백이 아닐 때 까지
        vertex = queue.popleft()        #큐에서 하나의 정점 vertex를 빼냄
        print(vertex,end="")            
        nbr=graph[vertex]-visited       #nbr: 차집합 연산 이용
        for v in nbr:
            visited.add(v)              #v방문
            queue.append(v)             #v를 큐에 삽입