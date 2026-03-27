# DP - 피보나치 수 2 (백준 브론즈 1)
# 문제 링크: https://www.acmicpc.net/problem/2748


# 완

import sys
input = sys.stdin.readline

def fibo(n, memo=None):
    if memo == None:
        memo = [None] * (n+2)
        memo[0] = 0
        memo[1] = 1

    if memo[n] != None:
        return memo[n]

    memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
    return memo[n]



print(fibo(int(input())))
