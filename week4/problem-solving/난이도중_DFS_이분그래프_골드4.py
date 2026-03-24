# DFS - 이분 그래프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/1707


import sys
input = sys.stdin.readline

from collections import deque

def make_graph(V, E):
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        v, e = map(int, input().split())
        graph[v].append(e)
        graph[e].append(v)
    return graph





k = int(input()) # 테스트 케이스
for i in range(k):
    V, E = map(int, input().split()) # V 정점 수 / E 간선 수
    graph = make_graph(V, E)
    v_colors = [0] * (V+1)

    for i in range(1, V+1):
        pass

