# 그리디 - 회의실 배정 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1931

# 완

import sys
input = sys.stdin.readline

N = int(input())

c_list = []
for _ in range(N):
    c_list.append(tuple(map(int, input().split())))

c_list = sorted(c_list, key=lambda x: (x[1], x[0])) # 시작과 동시에 끝나는 경우 고려

selected = []
selected.append(c_list[0])

for i in range(1, N):
    if c_list[i][0] >= selected[-1][1]:
        selected.append(c_list[i])

print(len(selected)) 