from UnionFind import *

def MSTKruskal(vertex,adj):#매개변수 : 정점리스트,인접행렬                 
    vsize = len(vertex)#정점의 개수
    init_set(vsize)#정점 집합 초기화
    eList = []#간선 리스트

    for i in range(vsize-1):#모든 간선을 리스트에 넣음
        for j in range(i+1,vsize):
            if adj[i][j] != None:
                eList.append((i,j,adj[i][j]))#튜플로 저장
#간선 리스트를 가중치의 내림차순을 정렬: 람다 함수 사용
    eList.sort(key=lambda e : e[2], reverse=True)

    edgeAccepted = 0
    while(edgeAccepted < vsize - 1): #정점 수 - 1개의 간선
        e = eList.pop(-1)#가장 작은 가중치를 가진 간선
        uset = find(e[0])#두 정점이 속한 집합 번호
        vset = find(e[1])

        if uset != vset:#두 정점이 다른 집합의 원소이면
            print("간선 추가 : (%s,%s,%d)"%(vertex[e[0]],vertex[e[1]],e[2]))#간선추가 출력
            union(uset,vset)#두 집합을 합함
            edgeAccepted += 1#간선이 하나 추가됨

vertex = ['A','B','C','D','E','F','G']
weight=[[None, 29, None, None, None, 10, None],
        [29, None, 16, None, None, None, 15],
        [None, 16, None, 12, None, None, None],
        [None, None, 12, None, 22, None, 18],
        [None, None, None, 22, None, 27, 25],
        [10, None, None, None, 27, None, None],
        [None, 15, None, 18, 25, None, None]]

print("MST By Kruskal's Algorithm")
MSTKruskal(vertex,weight)

