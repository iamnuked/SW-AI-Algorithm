# BFS - 미로 탐색 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/2178

'''
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오.
한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.
'''
from collections import deque


N, M = tuple(map(int, input().split()))

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input())))

q = deque()
q.append((0, 0))

# 오 아 왼 위
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while q:
    coord = q.popleft()
    r, c = coord
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if matrix[nr][nc] == 1:
                matrix[nr][nc] = matrix[r][c] + 1
                q.append((nr, nc))


print(matrix[N-1][M-1])