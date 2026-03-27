# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946


import sys
input = sys.stdin.readline

T = int(input())


for _ in range(T):
    N = int(input())
    score_list = []
    for i in range(N):
        score_list.append(tuple(map(int, input().split())))

    
