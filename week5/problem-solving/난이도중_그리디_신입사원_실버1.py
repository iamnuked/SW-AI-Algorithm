# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946


# 미완성

import sys
input = sys.stdin.readline

T = int(input())
result = []

for _ in range(T):
    N = int(input())

    score_list = []
    temp = set()
    for i in range(N):
        score_list.append(tuple(map(int, input().split())))
    
    score_list = sorted(score_list, key=lambda x: x[0])
    for score in score_list:
        if score_list[0][1] < score[1]:
            temp.add(score)

    score_list = sorted(score_list, key=lambda x: x[1])
    for score in score_list:
        if score_list[0][0] < score[0]:
            temp.add(score)

    result.append(len(score_list)-len(temp))

for i in result:
    print(i)

