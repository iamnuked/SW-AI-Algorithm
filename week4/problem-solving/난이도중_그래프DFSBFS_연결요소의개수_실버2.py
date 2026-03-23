# 그래프, DFS, BFS - 연결 요소의 개수 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/11724


'''
sys.stdin.readline이 더빠름
ㄴ 입력값이 많을 수록 그 격차가 더 커짐
ㄴ 이거 하나로 시간 초과에서 668ms 까지 줄어들음

'''

from collections import deque
import sys
input = sys.stdin.readline


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = True

    while q:
        v = q.popleft()

        for e in graph[v]:
            if visited[e] == False:
                visited[e] = True
                q.append(e)





N, M = map(int, input().split()) # N: 정점 수 / M: 간선 수

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


count = 0
# 그래프 삭제하는 방식 대신 visited 검사로 바꿔야 함
visited = [False] * (N+1)

for i in range(1, N+1):
    if visited[i] == False:
        bfs(i)
        count += 1


print(count)