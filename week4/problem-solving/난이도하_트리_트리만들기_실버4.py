# 트리 - 트리 만들기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/14244

# 완

'''
트리지만 그래프로 해석해야 할 듯 -> 사이클 판단 때문에 너무 복잡해짐 다시 트리로 접근
연결된 간선이 1개일 때 리프 노드
연결된 간선이 2개 이상일 때는 x

트리이기 때문에 사이클 생기면 안됨
그래프 차수로 계산?
0차수일 때 카운트 1업
사이클 판단은 어떻게 하지?

완전 이진트리에서 접근?
탐색하면서 돌아올때 카운트 1업 그러면 차수는 어떻게? -> 최대 리프 노드수 = 2^(차수-1) -> 노드 개수도 고려해야됨 -> 노드 개수만 생각하면 간단 하지만 트리가 너무 커짐
일단 노드 개수를 차수로 설정 -> 이러면 안됨 리프가 3개부터 모양이 안만들어짐 -> 3이상부터 차수 1씩 줄여야함


그냥 루트 노드에 추가하면 됨

Input : 5 3
Output : 0 1
         1 2
         1 3
         3 4
'''

def make_line_graph(node_count):
    edges = []
    for i in range(node_count-1):
        edges.append((i, i+1))
    return edges


def make_tree(node_count, leaf_count):
    edges = make_line_graph(node_count)
    count = 2 # 선 그래프에서 리프 노드 2개

    while leaf_count != count:
        # 끝 노드 루트 다음으로 이동
        # count++
        # edges[-1][0] = edges[1][0] 튜플은 내부 값 변경이 안되기 때문에 새로운 튜플 생성 후 대입해야 함
        edges[-1] = (edges[1][0], edges[-1][1]) # 마지막 노드 부모 노드를 두번째 노드값으로 변경 --> 문제 발생 옮긴 후 정렬 연산 들어가면며 너무 느려질 것 같음
        edges.sort()
        count += 1
    return edges

input_val = list(map(int, input().split()))
edges = make_tree(input_val[0], input_val[1])
for x in edges:
    a, b = x
    result = str(a) + " " + str(b)
    print(result)