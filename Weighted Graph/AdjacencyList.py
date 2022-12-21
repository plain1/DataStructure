graph={'A':set([('B',29),('F',10)]),
        'B':set([('A',29),('C',16),('G',15)]),
        'C':set([('B',16),('D',12)]),
        'D':set([('C',12),('E',22),('G',18)]),
        'E':set([('D',22),('F',27),('G',25)]),
        'F':set([('A',10),('E',27)]),
        'G':set([('B',15),('D',18),('E',25)])
}

def weightSum(graph):       #가중치의 총 합을 구하는 함수
    sum = 0                 
    for v in graph:         #그래프의 모든 정점v에 대해:'A','B',...
        for e in graph[v]:  #v의 모든 간선 e에 대해: ('B',29),...
            sum += e[1]     #sum에 추가
    return sum//2           #하나의 간선이 두 번 더해지므로 2로 나눔

def printAllEdges(graph):   #모든 간선을 출력하는 함수
    for v in graph:         #그래프의 모든 정점 v에 대해:'A','B',...
        for e in graph[v]:  #v의 모든 간선 e에 대해: ('B',29),...
            print("(%s,%s,%d)"%(v,e[0],e[1]),end='')

print('AL : weight sum = ',weightSum(graph))
printAllEdges(graph)