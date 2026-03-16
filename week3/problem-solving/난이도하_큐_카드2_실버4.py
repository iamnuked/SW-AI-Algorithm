# 큐 - 카드2 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/2164

# 완

# 시간 초과
# N = int(input())
# nums = []
# for i in range(1, N+1):
#     nums.append(i)

# while len(nums) != 1:
#     nums.pop(0)
#     if len(nums) == 1:
#         print(nums[0])
#         break
#     num = nums.pop(0)
#     nums.append(num)


from collections import deque
N = int(input())
q = deque()
for i in range(1, N+1):
    q.append(i)

if len(q) == 1:
    print(q[0])
else:
    while len(q) != 1:
        q.popleft()
        if len(q) == 1:
            print(q[0])
            break
        num = q.popleft()
        q.append(num)
