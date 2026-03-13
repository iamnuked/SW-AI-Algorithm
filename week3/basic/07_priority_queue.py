"""
[우선순위 큐 - 응급실 환자 관리]

문제 설명:
- 우선순위 큐를 사용하여 환자를 우선순위에 따라 처리합니다.
- 숫자가 작을수록 우선순위가 높습니다 (1 > 2 > 3).

입력:
- patients: (이름, 우선순위) 튜플 리스트

출력:
- 우선순위에 따라 처리된 환자 순서

예제:
입력: [("김철수", 3), ("이영희", 1), ("박민수", 2)]
출력:
처리: 이영희 (우선순위: 1)
처리: 박민수 (우선순위: 2)
처리: 김철수 (우선순위: 3)

힌트:
- heapq 모듈 사용
- heappush(): 힙에 추가
- heappop(): 최소값 제거
"""


'''
힙으로 구현하는 우선순위 큐는 완전 이진 트리 구조를 유지해야 됨 -> 중간에 빈 자리가 생기면 인덱스가 깨짐
예시
    1
   /  |
  3   ?
 /
7
[1, 3, ?, 7]

heappush는 무조건 순서대로 채워야 함(완전 이진 트리 유지)
heappop() 최소값 제거 후 마지막 노드 루트로 옮김 -> 그 후 정렬 -> 정렬 할 때 마지막 노드로 찾아가기 위해 왼쪽 오른쪽 판단 어떻게 하지?
''' 

import heapq

def process_emergency_room(patients):
    """
    환자를 우선순위에 따라 처리
    
    Args:
        patients: (이름, 우선순위) 리스트
    
    Returns:
        처리된 환자 순서
    """
    # TODO: 빈 힙 생성
    heap = []
    
    # TODO: 모든 환자를 힙에 추가
    for x in patients:
        data = x[0]
        order = x[1]
        heapq.heappush(heap, (order, data))
    pass
        
    processed = []
    
    # TODO: 힙이 비어있지 않은 동안 반복
    ## 힙에서 우선순위가 가장 높은 환자 꺼내기
    ## 환자 처리
    while len(heap) != 0:
        data = heapq.heappop(heap)
        print(f"처리: {data[1]} (우선순위: {data[0]})")
        processed.append(data[1])

    pass
        
    return processed

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    patients1 = [
        ("김철수", 3),
        ("이영희", 1),
        ("박민수", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result1 = process_emergency_room(patients1)
    print(f"처리 순서: {result1}")
    print()
    
    # 테스트 케이스 2
    patients2 = [
        ("환자A", 5),
        ("환자B", 1),
        ("환자C", 3),
        ("환자D", 2)
    ]
    print("=== 응급실 환자 처리 ===")
    result2 = process_emergency_room(patients2)
    print(f"처리 순서: {result2}")


