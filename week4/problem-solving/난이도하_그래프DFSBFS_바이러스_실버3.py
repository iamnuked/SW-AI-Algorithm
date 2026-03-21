# 그래프, DFS, BFS - 바이러스 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/2606

# 완

'''


'''

def make_graph(v, edges): # 그래프 초기화
    graph = {}
    
    for i in range(1, v+1):
        graph[i] = []

    for e in edges:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    return graph


def dfs(graph, start, visited=None):
    if visited == None:
        visited = []

    visited.append(start)
    for edge in graph[start]:
        if edge not in visited:
            dfs(graph, edge, visited)

    return visited

# def dfs(graph, start, visited=[]):

# 	visited.append(start)
	
# 	for edge in graph[start]:
# 		if edge not in visited:
# 			visited = dfs(graph, edge, visited)
			
# 	return visited


def worm(e, v, edges):
    count = 0
    graph = make_graph(v, edges)
    visited = dfs(graph, 1)
    return len(visited)




v = int(input())
e = int(input())

edges = []
for _ in range(e):
    edges.append(tuple(map(int, input().split())))

print(worm(e, v, edges)-1)
