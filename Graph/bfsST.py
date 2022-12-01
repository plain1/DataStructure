#신장 트리
import collections
def bfsST(graph,start):               
    visited = set([start])  #맨 처음에는 start만 방문한 정점
    queue = collections.deque([start]) #파이썬 컬렉션의 덱 생성(큐로 사용)
    while queue:        #공백이 아닐 때 
        v = queue.popleft() #큐에서 하나의 정점 v를 빼냄
        nbr = graph[v] - visited # nbr = {v의 인접정점} - {방문정점}
        for u in nbr:   #갈 수 있는 모든 인접 정점에 대해
            print("(",v,",",u,")",end="")   #(v,u)간선 추가
            visited.add(u)  #이제 u는 방문했음
            queue.append(u) #u를 큐에 삽입

mygraph = {"A":set(["B","C"]),
           "B":set(["A","D"]),
           "C":set(["A","D","E"]),
           "D":set(["B","C","F"],),
           "E":set(["C","H","G"],), 
           "F":set(["D"]),
           "G":set(["E","H"]),
           "H":set(["E","G"])
}

bfsST(mygraph,"A")