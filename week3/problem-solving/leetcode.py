class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode: # 재귀 호출용
        if not head or not head.next:
            return head
        

        # 1번은 한칸씩 2번은 두칸씩 이동해서 None 만났을 때 1번이 중간 값
        pointer1 = head
        pointer2 = head

        while pointer2.next != None:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            if pointer2.next == None: # 홀수인 경우 고려
                break
            pointer2 = pointer2.next

        pointer2 = pointer1.next # 오른쪽 head
        pointer1.next = None # 끊어주기

        
        pointer1 = self.sortList(pointer1) # 왼쪽 
        pointer2 = self.sortList(pointer2) # 오른쪽

        return self.merge(pointer1, pointer2)

    # 머지 정렬 함수 구현하세요~~
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        l_temp = ListNode()
        t_temp_head = l_temp

        while l1.next != None and l2.next != None:
            if l1.val <= l2.val:
                l_temp.next = l1
                l1 = l1.next
            else:
                l_temp.next = l2
                l2 = l2.next

            l_temp = l_temp.next

        if l1 == None:
            l_temp.next = l2
        elif l2 == None:
            l_temp.next = l1

        return t_temp_head
        pass

## 이하 테스트 케이스 생성용

def build_linked_list(values):
    dummy = ListNode()
    current = dummy

    for value in values:
        current.next = ListNode(value)
        current = current.next

    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result

test_cases = [
    [],
    [1],
    [4, 2, 1, 3],
    [-1, 5, 3, 4, 0],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [2, 2, 1, 1],
    [5, -2, 3, 0, -1],
]

solution = Solution()

for i, case in enumerate(test_cases, 1):
    head = build_linked_list(case)
    sorted_head = solution.sortList(head) # type: ignore
    result = linked_list_to_list(sorted_head)
    expected = sorted(case)

    print(f"Test {i}")
    print("input   :", case)
    print("result  :", result)
    print("expected:", expected)
    print("pass    :", result == expected)
    print()