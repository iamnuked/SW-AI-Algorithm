# DP - 동전 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9084


import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 복습 필요


'''

|  i  \  m  |  0 |  1 |  2 |  3 |  4 |
| --------- | -- | -- | -- | -- | -- |
| 0 (1원만)  |  1 |  1 |  1 |  1 |  1 |
| 1 (1원,2원)|  1 |  1 |  2 |  2 |  3 |


|     i \ m    |  0 |  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10 |
| ------------ | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- | -- |
| 0 (2)        |  1 |  0 |  1 |  0 |  1 |  0 |  1 |  0 |  1 |  0 |  1 |
| 1 (2, 3)     |  1 |  0 |  1 |  1 |  1 |  1 |  2 |  1 |  2 |  2 |  2 |
| 2 (2, 3, 5,) |  1 |  0 |  1 |  1 |  1 |  2 |  2 |  2 |  3 |  3 |  4 |



'''

def coin_dp(coins, M, memo=None):
    if memo == None:
        memo = [0] * (M+1)
        memo[0] = 1
    
    for c in coins:
        for i in range(c, M+1):
            memo[i] += memo[i-c]
    return memo[M]




T = int(input()) # T: 테스트 케이스  /  N: 동전 가지 수  /  M: 금액
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())


    print(coin_dp(coins, M))
    
    