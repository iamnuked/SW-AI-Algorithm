# DP - 01타일 (백준 실버3)
# 문제 링크: https://www.acmicpc.net/problem/1904

'''
N = 1 -> 1
N = 2 -> 2 (+1)
N = 3 -> 3 (+1)
N = 4 -> 5 (+2)
N = 5 -> 8 (+3)
N = 6 -> 13 (+5)
N = 7 -> 21 (+13)

??? 피보나치네

'''

# 완

N = int(input()) - 1

fibo = [1, 2, 3]


for i in range(N):
    fibo[i%3] = (fibo[(i+1)%3] + fibo[(i+2)%3]) % 15746 # 아주 큰 숫자를 리스트에 계속 대입할 경우 시간 비효율 발생

print(fibo[N%3])



















# 시간 초과

# import sys
# sys.setrecursionlimit(10**6)

# def comb(n, r):
#     result = 1
#     for i in range(r):
#         result *= (n-i)
#         result //= (i+1)
#     return result
    



# N = int(input())

# def f(N):
#     count = 0
#     r = 0
#     while N >= r:
#         count += comb(N, r)
#         N -= 1
#         r += 1
#     return count



# print(f(N)%15746)
