# DP - 평범한 배낭 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/12865

import sys
input = sys.stdin.readline

N, K = map(int, input().split()) # N 물품수, K 버틸 수 있는 무게

w_v_list = []

for i in range(N):
    w_v_list.append(tuple(map(int, input().split())))


