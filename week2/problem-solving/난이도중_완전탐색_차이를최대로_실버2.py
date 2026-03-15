# 완전탐색 - 차이를 최대로 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10819

'''
특징
맨 앞숫자는 한 번 더해짐 맨 뒷 숫자는 한 번 빼짐

절대값에 관하여
큰 수에서 작은 수 빼기 vs 작은 수에서 큰 수 빼기
|9-4| vs |4-9|는 5로 같은값이 나옴
결국 두 수의 차가 클수록 값은 크게 나옴

양 끝을 제외한 수들의 합은 어떤 조합이여도 다 같은 값이 나오는가?
9, 4, 3, 2, 5
[9, 4] [4, 3] [3, 2] [2, 5] = 5 + 1 + 1 + 3
[9, 3] [3, 4] [4, 2] [2, 5]= 6 + 1 + 2 + 3
결과는 x

9, 7, 6, 5, 2, 1
9, 7, 5, 6, 2, 1

[9, 7] [7, 6] [6, 5] [5, 2] [2, 1] = 2 + 1 + 1 + 3 + 1
[9, 7] [7, 5] [5, 6] [6, 2] [2, 1] = 2 + 2 + 1 + 4 + 1

순서가 뒤죽박죽일 때 값이 커짐 => 걍 노가다 해야됨
전체 조합 찾아서 최대값 찾기




'''

num = input()
nums = input()
nums = list(map(int, nums.split(" ")))



nums.sort(reverse=True)
print(nums)
if len(nums) % 2 == 0:
    for i in range(1, len(nums)//2-1, 2):
        temp = nums[i]
        nums[i] = nums[-(i+1)]
        nums[-(i+1)] = temp

else:
    for i in range(1, len(nums)//2, 2):
        temp = nums[i]
        nums[i] = nums[-(i+1)]
        nums[-(i+1)] = temp


print(nums)

sum = 0
for i in range(0, len(nums)-1):
    sum = sum + abs(nums[i] - nums[i+1])



print(sum)
