# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865


import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N 물품수, K 버틸 수 있는 무게

w_v_list = [] # (무게, 가치)

for i in range(N):
    w_v_list.append(tuple(map(int, input().split())))

dp = [[-1] * (K+1) for i in range(N+1)]

def ns(i, K): # i 번째 물건 인덱스, K 남은 무게
    if i == -1:
        return 0

    if dp[i][K] != -1:
        return dp[i][K]

    if (K-w_v_list[i][0]) < 0:
        dp[i][K] = ns(i-1, K)
        return dp[i][K]

    dp[i][K] = max(ns(i-1, K-w_v_list[i][0]) + w_v_list[i][1], ns(i-1, K))
    return dp[i][K]

print(ns(len(w_v_list)-1, K))