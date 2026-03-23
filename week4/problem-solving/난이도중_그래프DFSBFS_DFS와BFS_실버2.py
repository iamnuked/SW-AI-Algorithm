# 그래프, DFS, BFS - DFS와 BFS (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1260


'''
작은 숫자부터 방문

'''

from collections import deque
import sys
input = sys.stdin.readline



# def dfs(start):
#     stack = []
#     stack.append(start)
#     order = []

#     while stack:
#         temp_stack = []
#         v = stack.pop()
#         visited[v] = True
#         order.append(v)
#         for e in graph[v]:
#             if visited[e] == False:
#                 temp_stack.append(e)
#                 visited[e] = True
#         temp_stack.sort(reverse=True)
#         stack.extend(temp_stack)

#     return order

def dfs(start, visited):

    visited[start] = True
    order.append(start)
    sorted_edges = sorted(graph[start])
    for e in sorted_edges:
        if visited[e] == False:
            dfs(e, visited)

    return order
    




def bfs(start):
    q = deque()
    q.append(start)
    order = []
    
    while q:
        temp_q = deque()
        v = q.popleft()
        visited[v] = True
        order.append(v)
        for e in graph[v]:
            if visited[e] == False:
                temp_q.append(e)
                visited[e] = True
        temp_q = sorted(temp_q)
        q.extend(temp_q)
    return order



N, M, start = map(int, input().split())

# 그래프 만들기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

order = []
visited = [False] * (N+1)
print(' '.join(map(str, dfs(start, visited))))

visited = [False] * (N+1)
print(' '.join(map(str, bfs(start))))
