# 배열 - 평균은 넘겠지 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/4344

C = int(input())

result_list = []

for _ in range(C):
    N = input().split()
    count = 0
    avg = 0
    sum = 0
    for x in range(len(N)):
        N[x] = int(N[x])

    s_num = N[0]
    score_list = N[1:]
    
    for x in score_list:
        sum = sum + x

    avg = sum / s_num

    for x in score_list:
        if x > avg:
            count = count + 1

    result = (count / s_num)*100
    result_list.append(result)

for x in result_list:
    print(f"{x:.3f}%")
