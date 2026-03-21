# 그래프, DFS, BFS - 점프왕 쩰리 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/16173

'''
게임 오버 조건
if 점프칸 > N - idx:
    GAMEOVER

맵 -> matrix[N][N]

이동 옵션 오른쪽, 아래


오른쪽 이동
def move_right()
    return idx1, idx2

아래 이동
def move_down()
    return idx1, idx2

백트래킹으로 상태 저장? -> idx를 저장

stack에 r 저장
r pop 후 d 저장



dfs로 접근
'''
matrix = []
N = int(input())
for _ in range(N):
    matrix.append(list(map(int, input().split())))

visited = []
result = ["Hing"]

def dfs(r, c):
    coord = (r, c)
    jump = matrix[r][c]
    if jump == -1:
        result[0] = "HaruHaru"
        return 
    if coord in visited:
        return
    
    visited.append(coord)
    
    if jump < N - r:
        dfs(r + jump, c)

    if jump < N - c:
        dfs(r, c + jump)
    

dfs(0, 0)

print(result[0])  
