# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

'''
행렬에서 각 x,y요소를 한번씩만 선택

-> 조합 문제
경로가 같으면 어느 도시에서 시작하든 거리는 같음




'''
# city_count = input()
# city_matrix = input()

city_count = "4"
city_matrix1 = "0 10 15 20"
city_matrix2 = "5 0 9 10" 
city_matrix3 = "6 13 0 12"
city_matrix4 = "8 8 9 0"

city_matrix = []
city_matrix1 = city_matrix1.split(" ")
city_matrix2 = city_matrix2.split(" ")
city_matrix3 = city_matrix3.split(" ")
city_matrix4 = city_matrix4.split(" ")

city_matrix.append(city_matrix1)
city_matrix.append(city_matrix2)
city_matrix.append(city_matrix3)
city_matrix.append(city_matrix4)

print(city_matrix)

selected = []

def select_next(city :list):
    for i in range(len(city)):
        for j in range(i):

            if selected[j] == 1:
                selected.pop()

            if city_matrix[i][j] == 0:
                selected.pop()
            selected[j] == 1





 
import sys
n = int(input())

w = [list(map(int,input().split())) for _ in range(n)]
sums = [sys.maxsize]

def backtracking(start, visited):
    if (len(visited) == n):
        visited.append(visited[0])
        sum = 0
        for i in range(len(visited) -1):
            if (w[visited[i]][visited[i+1]] == 0):
                visited.pop()
                return
            sum += w[visited[i]][visited[i+1]]
        if sums[0] > sum:
            sums[0] = sum
        visited.pop()
        return

    for i in range(1, n):
        if i not in visited:
            visited.append(i)
            backtracking(visited[len(visited) -1], visited)
            visited.pop()

backtracking(0, [0])

print(sums[0])
