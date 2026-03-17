# 이분탐색 - 수 찾기 (백준 실버4)
# 문제 링크: https://www.acmicpc.net/problem/1920


# 완

N = int(input())
Ns = list(map(int, input().split()))


M = int(input())
Ms = list(map(int, input().split()))

# 출력 (시간 초과)
# for m in Ms:
#     if m in Ns:
#         print(1)
#     else:
#         print(0)


# 이진 탐색 필요


# 이것도 시간 초과
Ns.sort()

def binary_search(arr, target):
    start = 0
    end = len(arr)-1

    while start+1 != end:
        mid = (start+end) // 2
        if target == arr[mid]:
            return print(1)
        elif target > arr[mid]:
            start = mid
        elif target < arr[mid]:
            end = mid
        
    if arr[start] == target or arr[end] == target:
        return print(1)

    return print(0)

    

for m in Ms:
    binary_search(Ns, m)

# arr = [1, 2, 3, 4, 5]
# binary_search(arr, 6)