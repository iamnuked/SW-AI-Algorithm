# 그리디 - 신입 사원 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/1946


# 미완성

# import sys
# input = sys.stdin.readline

# T = int(input())
# result = []

# for _ in range(T):
#     N = int(input())

#     score_list = []
#     temp = set()
#     for i in range(N):
#         score_list.append(tuple(map(int, input().split())))
    
#     score_list = sorted(score_list, key=lambda x: x[0])
#     for score in score_list:
#         if score_list[0][1] < score[1]:
#             temp.add(score)

#     score_list = sorted(score_list, key=lambda x: x[1])
#     for score in score_list:
#         if score_list[0][0] < score[0]:
#             temp.add(score)

#     result.append(len(score_list)-len(temp))

# for i in result:
#     print(i)



import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    score_list = []
    for i in range(N):
        score_list.append(tuple(map(int, input().split())))
    
    score_list.sort(key=lambda x: x[0])

    count = 0
    min_score = N
    for score in score_list:
        if score[1] <= min_score:
            count += 1
            min_score = score[1]

    print(count)

##############################################

# import sys
# input = sys.stdin.readline

# T = int(input())
# result = []

# for _ in range(T):
#     N = int(input())

#     score_list = []
#     for i in range(N):
#         score_list.append(tuple(map(int, input().split())))

#     paper_sorted = sorted(score_list, key=lambda x: x[0])

#     interview_sorted = sorted(score_list, key=lambda x: x[1])

#     interview_rank = {}
#     for i in range(N):
#         interview_rank[interview_sorted[i]] = i

#     count = 0
#     min_rank = N

#     for score in paper_sorted:
#         if interview_rank[score] < min_rank:
#             count += 1
#             min_rank = interview_rank[score]

#     result.append(count)

# for i in result:
#     print(i)



#     interview_rank = {
#     (4,1): 0,
#     (3,2): 1,
#     (2,3): 2,
#     (1,4): 3 }
#
#  score_list
#
# paper_sorted  (서류 기준 정렬)
# interview_sorted ->  interview_rank (면접 순위표)
#
# for score in paper_sorted:
#     interview_rank[score] vs min_rank 비교