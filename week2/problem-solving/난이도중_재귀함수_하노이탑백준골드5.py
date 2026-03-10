# 재귀함수 - 하노이 탑 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/1914


'''
원판을 정렬하는 규칙
가장 작은 원판 정렬 부터 시작
n을 옮기기 위해서 n-1 원판을 정렬 해야됨


이동에 관한 규칙

원판 3개 순서
1 -> 2
1 -> 3
2 -> 3
1 -> 2
3 -> 1
3 -> 2
1 -> 2
4번째 원판 1 -> 3

원판 2개 순서
1 -> 2
1 -> 3
2 -> 3
3번째 원판 1 -> 2

원판 1개 순서
1 -> 2
2번째 원판 1 -> 3

규칙 1
첫 시작은 두 기둥중 아무거나 선택한다 -> 두 기둥 모두 가장 큰 원판(빈 기둥)이기 때문

규칙 2


작 큰
작 큰
작 작
작 큰

작 작
작 큰
작 작
작 큰
작 큰
작 작

작 작

원판을 두 블럭으로 나눈다면
-> 가장 가장 큰 원판 + 나머지 원판

나머지 원판 -> 가장 큰 원판 + 나머지 원판

빈 기둥 옮길 기둥이 중요함




        
기둥을

오케이 시작
'''

    


# def hanoi(n, now, target):
#     if n == 0:
#         return
    
#     now, target = move(now, target)
    
#     hanoi(n-1, now, target)


# def move(now, target):
#     empty = 6-now-target
#     print(now, empty)
#     print(now, target)
#     print(empty, target)
#     print(now, empty)

#     temp = now
#     now = target
#     target = empty
#     empty = temp

#     return now, target



# hanoi(int(input()), 1, 3)
'''
원판 이동
1 -> 2 
1 -> 3
2 -> 1
2 -> 3
1 -> 2
1 -> 3

'''


def hanoi(n, now, target, temp):
    if n == 1: # 마지막 1번 원판: 현재 -> 타겟
        print(now, target)
        return
    hanoi(n-1, now, temp, target) # n-1개 원판 현재 -> temp로
    hanoi(n-1, temp, target, now) # n-2 원판 temp -> 




hanoi(int(input()), 1, 3, 2)