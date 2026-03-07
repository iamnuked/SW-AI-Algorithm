# 파이썬 문법 - 최댓값 (백준 브론즈3)
# 문제 링크: https://www.acmicpc.net/problem/2562

num_list = []

for i in range(9):
    num = input()
    num_list.append(int(num))

num = 0
count = 0
i = 1
for x in num_list:
    if num < x:
        num = x
        count = i
    i = i + 1

print(num)
print(count)

