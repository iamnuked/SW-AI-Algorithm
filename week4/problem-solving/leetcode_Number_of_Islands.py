# https://leetcode.com/problems/number-of-islands/description/?envType=study-plan-v2&envId=top-interview-150

# 미완

from collections import deque
import copy

class Solution:
    def __init__(self):
        # 오 아 왼 위
        self.dr = [0, 1, 0, -1]
        self.dc = [1, 0, -1, 0]
        self.search_p = (0, 0)
        self.visited = []
        self.grid = []
        self.count = 0

    def numIslands(self, grid) -> int:
        N = len(grid)
        M = len(grid[0])
        self.grid = grid
        self.visited = [[False] * M for _ in range(N)]

        while self.search_p != (N-1, M-1):
            self.bfs(self.search_p, N, M)
            self.count += 1
            self.search(N, M)

        return self.count


    def bfs(self, start, N, M):
        q = deque()
        q.append(start)
        r, c = start
        self.visited[r][c] = True

        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + self.dr[i]
                nc = c + self.dc[i]
                if 0 <= nr < N and 0 <= nc < M:
                    if self.visited[nr][nc] == False and self.grid[nr][nc] == "1":
                        q.append((nr, nc))
                        self.visited[nr][nc] == True


    def search(self, N, M):
        r, c = self.search_p
        for x in range(r, N):
            start_y = c if x == r else 0
            for y in range(start_y, M):
                if self.visited[x][y] == False and self.grid[x][y] == "1":
                    self.search_p = (x, y)
                    return

