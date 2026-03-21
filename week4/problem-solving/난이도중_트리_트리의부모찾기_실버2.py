# 트리 - 트리의 부모 찾기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(10**6)


def make_graph(N, edges):
    graph = {}
    for i in range(1, N+1):
        graph[i] = []

    for e in edges:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)

    return graph



def find_p(graph, v, p):
    if graph[v]:
        return
    p_dict[v] = p
    graph[v].remove(p)
    for e in graph[v]:
        find_p(graph, e, v)
    return

p_dict = {}
N = int(input())

edges = []
for _ in range(N-1):
    edges.append(tuple(map(int, input().split())))

graph = make_graph(N, edges)
for e in graph[1]:
    find_p(graph, e, 1)

result = list(p_dict.items())

result = sorted(result)
for x in result:
    print(x[1])
