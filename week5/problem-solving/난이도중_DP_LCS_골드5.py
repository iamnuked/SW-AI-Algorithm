# DP - LCS (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/9251


str1 = input()
str2 = input()


lcs = [ [0] * (len(str1) + 1) for _ in range(len(str2) + 1) ]

for y in range(1, len(str2)+1):
    for x in range(1, len(str1)+1):
        if str1[x-1] == str2[y-1]:
            lcs[y][x] = lcs[y][x-1] + 1
            break
        else:
            lcs[y][x] = lcs[y][x-1]


print(lcs)
    