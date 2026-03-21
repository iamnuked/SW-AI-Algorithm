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


'''

def move_right(idx1, idx2, matrix, N, stack):
    stack.append((idx1, idx2))
    if matrix[idx1][idx2] > N - idx1:
        stack.pop()
        return

    idx1 = idx1 + matrix[idx1][idx2]

    if matrix[idx1][idx2] == -1:
        return "HaruHaru"
    
    return idx1, idx2 # 이동한 칸 idx


def move_down(idx1, idx2, matrix, N, stack):
    if matrix[idx1][idx2] > N - idx2:
        stack.pop()
        return

    idx2 = idx2 + matrix[idx1][idx2]
    if matrix[idx1][idx2] == -1:
        return "HaruHaru"
    
    return idx1, idx2





def jump_jjelly(matrix, N, idx1=0, idx2=0):
    stack = []
    stack.append((idx1, idx2))
    


    pass



N = 3
matrix = [[1, 1, 10], [1, 5, 1], [2, 2, -1]]

print(jump_jjelly(matrix, N))