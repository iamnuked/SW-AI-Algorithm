# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

'''
N = 1 -> 1
N = 2 -> 2 (+1)
N = 3 -> 3 (+1)
N = 4 -> 5 (+2)
N = 5 -> 8 (+3)
N = 6 -> 13 (+5)


'''

import sys
sys.setrecursionlimit(10**6)

def comb(n, r):
    result = 1
    for i in range(r):
        result *= (n-i)
        result //= (i+1)
    return result
    



N = int(input())

def f(N):
    count = 0
    r = 0
    while N >= r:
        count += comb(N, r)
        N -= 1
        r += 1
    return count



print(f(N)%15746)