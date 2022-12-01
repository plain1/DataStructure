#연결 성분 검사
def find_connected_component(graph):
    visited = set() #이미 방문한 정점 집합
    colorList = []  #부분 그래프별 정점 리스트

    for vtx in graph:   #그래프의 모든 정점들에 대해
        if vtx not in visited:  #방문하지 않은 정점이 있으면
            color = dfs_cc(graph,[],vtx,visited)    #새로운 컬러리스트
            colorList.append(color) #컬러 리스트 추가

    print("그래프 연결성분 개수 = %d"%len(colorList))
    print(colorList)    #정점 리스트들을 출력

def dfs_cc(graph,color,vertex,visited): 
    if vertex not in visited:   #아직 칠해지지 않은 정점에 대해
        visited.add(vertex)     #이제 방문
        color.append(vertex)    #같은 색의 정점 리스트에 추가
        nbr = graph[vertex]-visited #nbr: 차집합 연산 이용
        for v in nbr:
            dfs_cc(graph,color,v,visited) #순환 호출
    return color    #같은 색의 정점 리스트 반환

mygraph = {"A":set(["B","C"]),
           "B":set(["A"]),
           "C":set(["A"]),
           "D":set(["E"]),
           "E":set(["D"])
    }

print('find_connected_component: ')
find_connected_component(mygraph)