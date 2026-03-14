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









# 배열을 피벗 기준으로 분할하는 함수 -> lomuto 분할
# arr: 배열, low: 시작 인덱스 high: 끝 인덱스
def partition(arr, low, pivot_idx):
    stop_idx = low
    for i in range(low, pivot_idx):
        if arr[i] > arr[pivot_idx]:
            for o in range(i+1, pivot_idx):
                if arr[o] < arr[pivot_idx]:
                    temp = arr[o]
                    arr[o] = arr[stop_idx]
                    arr[stop_idx] = temp
                    stop_idx = stop_idx + 1
            break
        else:
            stop_idx = stop_idx + 1


    # stop값 pivot값 교환
    temp = arr[stop_idx]
    arr[stop_idx] = arr[pivot_idx]
    arr[pivot_idx] = temp



    
    return stop_idx # 피벗의 최종 위치 인덱스



# 퀵 정렬 재귀 함수
# arr: 배열, low: 시작 인덱스 high: 끝 인덱스
def quick_sort_helper(arr, low, high):

    if low <= high:    
        pivot_idx = partition(arr, low, high)
        quick_sort_helper(arr, low, pivot_idx-1)
        quick_sort_helper(arr, pivot_idx+1, high)

    return
    



# 퀵 정렬 메인 함수
def quick_sort(arr):
    
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


