# 그리디 - 잃어버린 괄호 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1541

'''
55-50+40+20-50+10 -> 최소 55-(50+40+20)-(50+10)

-로 스플릿
+로 스플릿 후 sum
첫번째 - sum1 -sum2 ...

'''

# 완

split_by_minus = input().split('-')

sums = []
for x in split_by_minus:
    sums.append(sum(map(int, x.split('+'))))

result = sums[0]
for i in range(1, len(sums)):
    result -= sums[i]

print(result)

