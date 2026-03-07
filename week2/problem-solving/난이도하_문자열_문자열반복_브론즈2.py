# 문자열 - 문자열 반복 (백준 브론즈2)
# 문제 링크: https://www.acmicpc.net/problem/2675

result_list = []
T = int(input())

for _ in range(T):
    arr = input().split()
    rep = int(arr[0])
    string = arr[1]
    result = ""
    for x in string:
        for _ in range(rep):
            result = result + x

    result_list.append(result)

for x in result_list:
    print(x)


