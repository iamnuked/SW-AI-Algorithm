"""
[머지 정렬 구현]

문제 설명:
- 머지 정렬(Merge Sort) 알고리즘을 구현합니다.
- 분할 정복(Divide and Conquer) 방식을 사용합니다.
- 배열을 절반으로 나누고, 각각을 정렬한 후 병합합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [38, 27, 43, 3, 9, 82, 10]
출력: [3, 9, 10, 27, 38, 43, 82]

힌트:
- 배열을 절반으로 분할 (재귀)
- 각 부분을 재귀적으로 정렬
- 정렬된 두 부분을 병합
"""





# 두 개의 정렬된 부분 배열을 병합하는 함수
# arr: 원본 배열 left: 왼쪽 부분의 시작 인덱스 mid: 왼쪽 부분의 끝 인덱스 right: 오른쪽 부분의 끝 인덱스
def merge(arr, left, mid, right):
    l_arr = arr[left:mid+1]
    r_arr = arr[mid+1:right+1]
    lp = 0
    rp = 0
    k = left
    le = len(l_arr)
    re = len(r_arr)

    while lp < le and rp < re:
        if l_arr[lp] <= r_arr[rp]:
            arr[k] = l_arr[lp]
            lp += 1
        else:
            arr[k] = r_arr[rp]
            rp += 1
        k += 1

    while lp < le:
        arr[k] = l_arr[lp]
        k += 1
        lp += 1

    while rp < re:
        arr[k] = r_arr[rp]
        k += 1
        rp += 1




# 머지 정렬 재귀 함수
# arr: 배열, left: 시작 인덱스, right: 끝 인덱스
def merge_sort_helper(arr, left, right): # left, right는 idx
    mid = (left + right) // 2
    # base case
    if left >= right:
        return
        # 재귀 호출

    merge_sort_helper(arr, left, mid)
    merge_sort_helper(arr, mid+1, right)
    merge(arr, left, mid, right)
    

# 머지 정렬 메인 함수
def merge_sort(arr):

    if len(arr) > 1:
        merge_sort_helper(arr, 0, len(arr) - 1)
    return arr



# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [38, 27, 43, 3, 9, 82, 10]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = merge_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [12, 11, 13, 5, 6, 7]
    print("=== 테스트 케이스 2 ===")
    print(f"정렬 전: {arr2}")
    result2 = merge_sort(arr2.copy())
    print(f"정렬 후: {result2}")
    print()
    
    # 테스트 케이스 3: 역순
    arr3 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = merge_sort(arr3.copy())
    print(f"정렬 후: {result3}")
    print()
    
    # 테스트 케이스 4: 중복 원소
    arr4 = [5, 2, 8, 2, 9, 1, 5, 5]
    print("=== 테스트 케이스 4: 중복 원소 ===")
    print(f"정렬 전: {arr4}")
    result4 = merge_sort(arr4.copy())
    print(f"정렬 후: {result4}")


