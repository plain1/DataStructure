parent = []                 #각 노드의 부모노드 인덱스
set_size = 0                #전체 집합의 개수

def init_set(nSets):        #집합의 초기화 함수
    global set_size, parent #전역변수 사용(변경)을 위함
    set_size = nSets        #집합의 개수
    for i in range(nSets):  #모든 집합에 대해
        parent.append(-1)   #각각이 고유의 집합(부모가-1)

def find(id):               #정점 id가 속한 집합의 대표번호 탐색
    while (parent[id]>=0):  #부모가 있는 동안(-1이 아닌 동안)
        id = parent[id]     #id를 부모 id로 갱신
    return id               #최종 id 반환, 트리의 맨 위 노드의 id임

def union(s1,s2):           #두 집합을 병합(s1을 s2에 병합시킴)
    global set_size         #전역변수 사용(변경)을 위함
    parent[s1] = s2         #s1을 s2에 병합시킴
    set_size = set_size - 1 #집합의 개수가 줄어 듦



    


