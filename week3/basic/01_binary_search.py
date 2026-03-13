"""
[이분 탐색 - Binary Search]

문제 설명:
- 정렬된 배열에서 특정 값을 찾는 이분 탐색 알고리즘을 구현합니다.
- 배열을 반으로 나누어 탐색 범위를 절반씩 줄여갑니다.

입력:
- arr: 정렬된 정수 배열
- target: 찾고자 하는 값

출력:
- target이 있는 인덱스 (없으면 -1)

예제:
입력: arr = [1, 3, 5, 7, 9, 11, 13], target = 7
출력: 3

힌트:
- left, right 포인터 사용
- mid = (left + right) // 2
- arr[mid]와 target 비교하여 범위 조정
"""

'''
이분 탐색, 이진 탐색 용어
보통 같은말로 사용 -> 뉘양스 차이

이진 탐색 핵심
1. 정렬된 배열에서 가능
2. 배열을 반으로 나누어 탐색 범위를 줄임 -> 시간 복잡도 logN
3. 배열 중간에서 시작 -> 그러면 홀/짝수 구분 해야하나? -> 내 생각엔 포인터 이동시 +1, -1 작업 있을 때 필요할 것 같은데 포인터 이동 안하는 경우는 필요 없을 것 같음
4. 중간값 목표값 비교해서 왼쪽 오른쪽 선택

의문점
1. 문제에서는 이진 탐색 인자값으로 정렬된 배열이 들어가는데 실제로 이진 탐색 구현시 배열 정렬 과정을 이진 탐색 내부에 작성하지 않아도 되는건지
2. 왼쪽 오른쪽 이동시 +1, -1 작업이 꼭 필요한지

'''

def binary_search(arr, target):
    """
    이분 탐색 구현
    
    Args:
        arr: 정렬된 배열
        target: 찾을 값
    
    Returns:
        target의 인덱스 (없으면 -1)
    """

    left = 0
    right = len(arr) - 1
    
    # TODO: left가 right보다 작거나 같을 때까지 반복
    ## 중간 인덱스 계산
    ## arr[mid]와 target 비교
    ## 같으면 mid 반환
    ## target이 더 크면 left = mid + 1
    ## target이 더 작으면 right = mid - 1

    while left+1 != right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        elif target < arr[mid]: # 왼쪽으로 이동
            right = mid  
        elif arr[mid] < target: # 오른쪽으로 이동
            left = mid


    
    return -1 # 없는 경우

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [1, 3, 5, 7, 9, 11, 13]
    target1 = 7
    result1 = binary_search(arr1, target1)
    print(f"배열: {arr1}")
    print(f"찾는 값: {target1}")
    print(f"결과: 인덱스 {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target2 = 14
    result2 = binary_search(arr2, target2)
    print(f"배열: {arr2}")
    print(f"찾는 값: {target2}")
    print(f"결과: 인덱스 {result2}")
    print()
    
    # 테스트 케이스 3: 없는 값
    arr3 = [1, 3, 5, 7, 9]
    target3 = 6
    result3 = binary_search(arr3, target3)
    print(f"배열: {arr3}")
    print(f"찾는 값: {target3}")
    print(f"결과: 인덱스 {result3}")
