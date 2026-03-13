"""
[퀵 정렬 구현]

문제 설명:
- 퀵 정렬(Quick Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 피벗(pivot)을 기준으로 작은 값과 큰 값을 분할하여 재귀적으로 정렬합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [10, 7, 8, 9, 1, 5]
출력: [1, 5, 7, 8, 9, 10]

힌트:
- 피벗 선택 (일반적으로 마지막 원소)
- 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 분할
- 재귀적으로 왼쪽과 오른쪽 부분 정렬
"""

'''
피벗이 무엇인가? -> 분할 하는 기준점 -> 피벗 값에 따라 성능이 달라짐 -> 왼쪽 오른쪽 크기가 비슷해야 성능이 좋아지나?(검증 필요)
피벗 선택 기준은? 
분할 -> 정렬  무한 반복?
순서
헬퍼 호출 -> 파티션 호출

피벗 값은 정렬 필요 x 이미 중간 값이기 때문

이 문제는 Lomuto partition 방식 -> 구현 쉬움 swap이 많이 발생 -> 이유는?
Hoare partition 방식은 구현 어려움 swap 횟수가 적음 -> 이유는?
'''

def partition(arr, low, high):
    """
    배열을 피벗 기준으로 분할하는 함수
    
    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    
    Returns:
        피벗의 최종 위치 인덱스
    """
    # TODO: 피벗을 선택 (일반적으로 마지막 원소)
    pivot_v = arr[high]
    
    # TODO: i는 작은 원소들의 마지막 인덱스를 추적 ---> i+1은 (큰 원소들의 시작점) (아닌듯?)
    i = low

    # TODO: low부터 high-1까지 순회하면서
    ## 현재 원소가 피벗보다 작거나 같으면:
    ##   1. i를 1 증가
    ##   2. arr[i]와 arr[j]를 교환

    for j in range(low, high+1):
        if arr[j] <= pivot_v:
            i = i + 1

            if i != j: # 여기서 i는 예비 pivot 자리 왼쪽
                temp = arr[i]
                arr[i] == arr[j]
                arr[j] == temp
    
    # TODO: 피벗을 올바른 위치(i+1)에 배치
    if high == i:
        return -1
    

    temp = arr[i]
    arr[i] = arr[i+1] # 여기까지 구현
    arr[i+1] = temp
    
    return i + 1

# 시작할 때 len(arr)-1 로 시작했음 -> pivot != high
def quick_sort_helper(arr, low, high): # 재귀 호출 용도인 듯
    """
    퀵 정렬 재귀 함수
    
    Args:
        arr: 배열
        low: 시작 인덱스
        high: 끝 인덱스
    """
    # TODO: base case - low가 high보다 작을 때만 정렬
    if high - high == 0: # 길이가 1인 경우 -> 필요한 것 같은데 정확히는 모르겠음. 다 풀고 확인 해야 함
        return

    if high - low == 1: # 정복 -> 분할된 길이가 2인 경우
        if arr[low] < arr[high]:
            temp = arr[low]
            arr[low] = arr[high]
            arr[high] = temp
        return
    

    ## 분할하여 피벗 인덱스 얻기
    pivot_idx = partition(arr, low, high)
    if pivot_idx == -1:
        return

    ## 피벗 왼쪽 부분 재귀 정렬
    quick_sort_helper(arr, low, pivot_idx-1)
    ## 피벗 오른쪽 부분 재귀 정렬
    quick_sort_helper(arr, pivot_idx+1, high)
    

    return
    

def quick_sort(arr):
    """
    퀵 정렬 메인 함수
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [10, 7, 8, 9, 1, 5]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = quick_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = quick_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 중복 원소
    arr3 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print("=== 테스트 케이스 3: 중복 원소 ===")
    print(f"정렬 전: {arr3}")
    result3 = quick_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 이미 정렬된 배열
    arr4 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 4: 이미 정렬됨 ===")
    print(f"정렬 전: {arr4}")
    result4 = quick_sort(arr4.copy())
    print(f"정렬 후: {result4}")
    print("이미 정렬된 경우 O(n²) 시간 소요 (최악의 경우)")


