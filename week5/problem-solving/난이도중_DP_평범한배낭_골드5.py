# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N 물품수, K 버틸 수 있는 무게

w_v_list = []

for i in range(N):
    w_v_list.append(tuple(map(int, input().split())))


dp = [[[0,0]] * (K+1) for i in range(N)]

for i, wv in enumerate(w_v_list):
    for w in range(K+1):
        if wv[0] <= w - dp[i][w][0]: # 추가 무게 남은 무게 비교
            dp[i][w][0] += wv[0] # 무게
            dp[i][w][1] += wv[1] # 가치


print(dp)

