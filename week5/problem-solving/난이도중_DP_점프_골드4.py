# DP - 점프 (백준 골드4)
# 문제 링크: https://www.acmicpc.net/problem/2253


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = [0] * (N + 2) # 0번 더미, N+1 인덱스는 마지막에서 가속된 결과 저장
memo[1] = 1
memo[2] = 1

for _ in range(M):
    memo[int(input())] = None


# def jump(n, memo):
#     i = 2
#     x = 1
#     while i < n:
#         memo[i] = min([ memo[n-(x-1)], memo[n-x], memo[n-(x+1)] ])
#         i += 

#     return memo[n]
#     pass



def jump(n, x): # 마지막일 때 속도는?

    if memo[n] != 0:
        memo[n] = min([jump(n-(x-1), x-1), jump(n-x, x), jump(n-(x+1), x+1)]) + 1

    return memo[n]

