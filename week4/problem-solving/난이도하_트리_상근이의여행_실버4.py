# 트리 - 상근이의 여행 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/9372

# 완

'''
모든 정점을 방문하는데 필요한 최소의 간선 수는 정점-1개
'''

case_count = int(input())
v_count = []
for _ in range(case_count):
    NM = list(map(int, input().split()))
    v_count.append(NM[0])
    for _ in range(NM[1]):
        input()
    
for x in v_count:
    print(x-1)