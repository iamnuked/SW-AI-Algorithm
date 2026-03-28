# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def coin_dp(coins, M, memo=None):
    if memo == None:
        memo = [0] * (M+len(coins))
        for i, v in enumerate(coins):
            memo[i] = v
    
    if memo[M] != 0:
        return memo[M]
    
    for i in coins:
        memo[M] += coin_dp(coins, M-i, memo)
    
    return memo[M]


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    print(coin_dp(coins, M))
    
    

