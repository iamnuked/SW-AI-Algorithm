# union & find


# 루트 노드 찾기
def find(v):
    if p[v] != v:
        return find(p[v])
    return v
    
# 두 트리 합치기 -> 루트끼리 병합
def union(a, b):
    v1 = find(a)
    v2 = find(b)

    p[v2] = v1
    pass




v = int(input())

p = [None] * (v+1)

for i in range(1, v+1):
    p[i] = i


union(2, 3)

print(p)