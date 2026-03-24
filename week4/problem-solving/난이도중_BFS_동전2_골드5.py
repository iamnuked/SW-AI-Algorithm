# BFS - 동전 2 (백준 골드5)
# 문제 링크: https://www.acmicpc.net/problem/2294

'''
bfs 사용

1. 루트 노드 생성
2. popleft
3. pop_node에서 가능한 코인 종류 만큼 임시에 큐 추가
4. 임시 큐 사이즈 계산
5. 큐에 추가
6. depth++
7. 큐 사이즈만큼 반복


자료형
cost_list = [] -> 동전 종류
node = [cost, sum, depth] -> 트리 노드(리스트)
q_temp = deque() -> q에 추가하기 전 cost 체크, sum체크 후 q_temp에 추가 -> len(q_temp) = q_size 큐 사이즈만큼 반복문 후 depth++

가치가 같은 동전 여러번 주어질 수도 있음. -> set으로 만들고 다시 리스트로 하면 동전 수 줄일 수 있음


'''


import sys
input = sys.stdin.readline

from collections import deque

################### 메모리 초과 #########################

n, k = map(int, input().split()) # n 동전 종류 수, k 타켓

cost_list = set()
for _ in range(n):
    cost_list.add(int(input()))

cost_list = list(cost_list)

def bfs(cost_list, target):
    q = deque()
    q.append([max(cost_list), 0]) # 루트 노드
    depth = 0
    while q:
        depth += 1
        q_size = len(q)
        for _ in range(q_size):
            p_node = q.popleft()
            for cost in cost_list:
                if cost <= p_node[0]:
                    sum = p_node[1] + cost
                    if sum == target:
                        return depth
                    elif sum < target:
                        q.append([cost, sum])

    return -1


print(bfs(cost_list, k))

########################################################

