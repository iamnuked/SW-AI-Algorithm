# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630



# test case

N = 8
matrix =   [[1, 1, 0, 0 ,0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1]]


# 길이는 무조건 짝수 맞음 2의 배수로 조건 주어짐 ->

# 해당 2차원 배열 다른 값 있는지 확인 후 있으면 cut


# 재귀로 가보자
def cut(matrix, start, end):


    


    pass

def check(matrix, start, end):
    first = matrix[start[0]][start[1]] # 첫번째 값
    for x in matrix: # 
        if x != first:
            cut(matrix)
            return
    

    pass


