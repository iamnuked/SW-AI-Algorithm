"""
[삽입 정렬 구현]

문제 설명:
- 삽입 정렬(Insertion Sort) 알고리즘을 구현합니다.
- 정렬된 부분에 새로운 원소를 적절한 위치에 삽입하는 방식입니다.
- 카드 게임에서 손에 든 카드를 정렬하는 방식과 유사합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [12, 11, 13, 5, 6]
출력: [5, 6, 11, 12, 13]

힌트:
- 첫 번째 원소는 이미 정렬되어 있다고 가정
- 두 번째 원소부터 시작하여 앞의 정렬된 부분에 삽입
- 삽입 위치를 찾기 위해 뒤에서 앞으로 비교
"""

def insertion_sort(arr):
    """
    삽입 정렬 구현
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    # TODO: 두 번째 원소(인덱스 1)부터 시작
    ## 각 원소를 정렬된 부분에 삽입
    ## 현재 원소를 key에 저장
    ## key를 삽입할 위치 찾기
    ## j는 key 바로 앞 인덱스부터 시작
    ## arr[j] > key인 동안 원소를 오른쪽으로 이동
    ## 찾은 위치에 key 삽입

    '''
    1. # 1번 인덱스부터 시작
    2. n번에서 n-1번 비교 -> n번이 더 크면 n+1번을 n-j번과 비교 -> n+1번이 n-j번보다 크다면 n-j에 삽입
    3. 삽입에 대한 연산은 어떻게? 원하는 인덱스에 삽입하는 메서드 있나? -> insert(인덱스, 값) 메서드 사용
    4. 삽입하는 과정: 삽입 값을 temp에 저장 -> 삽입 값 삭제 -> insert 메서드로 원하는 위치에 temp 삽입

    for i in range(1, n):
        curr = i
        prev = i-1
        if arr[curr] < arr[prev]:
            temp = arr[curr]
            arr.pop(curr)
            for j in range(curr+1):
                comp = i-1-j
                if comp == -1:
                    arr.insert(0, temp)
                    break
                if temp >= arr[comp]:
                    arr.insert(comp+1, temp)
                    break
    위 코드는 삽입정렬이 아님
    1. pop / insert 사용으로 리스트 길이 변화
    2. for문으로 탐색과정을 사용 -> 삽입 정렬은 쉬프트 방식을 사용해야됨(밀어내기)
    '''

    for i in range(1, n):
        curr = i
        prev = i-1
        temp = arr[i]
        while curr > 0 and temp < arr[prev]: # 맨 앞까지 간 경우 또는 이전 값이 지금 값보다 작은 경우 탈출
            arr[curr] = arr[prev]
            prev -= 1
            curr -= 1
        arr[curr] = temp

    return arr




"""
과정을 출력하는 삽입 정렬
"""
def insertion_sort_with_steps(arr):
    n = len(arr)
    print(f"초기 배열: {arr}")
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1 # 이전

        print(f"\nStep {i}: key = {key}")
        print(f"정렬된 부분: {arr[:i]}")

        # TODO: 삽입 위치 찾기 및 이동
        while i > 0 and key < arr[j]:
            arr[i] = arr[j]
            i -= 1
            j -= 1
        pass
        
        arr[i] = key
        print(f"삽입 후: {arr}")
    
    return arr
















# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [12, 11, 13, 5, 6]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = insertion_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()

    # 테스트 케이스 2: 과정 출력
    arr2 = [5, 2, 4, 6, 1, 3]
    print("=== 테스트 케이스 2: 정렬 과정 ===")
    result2 = insertion_sort_with_steps(arr2.copy())
    print()
    
    # 테스트 케이스 3: 이미 정렬된 배열
    arr3 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 3: 이미 정렬됨 ===")
    print(f"정렬 전: {arr3}")
    result3 = insertion_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print("이미 정렬된 경우 O(n) 시간 소요")


