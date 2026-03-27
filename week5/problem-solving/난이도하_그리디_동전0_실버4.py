# 그리디 - 동전 0 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/11047


# 완

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))
    

count = 0
coins.sort(reverse=True)
for c in coins:
    if K == 0:
        break
    count = count + K // c
    K %= c


print(count)