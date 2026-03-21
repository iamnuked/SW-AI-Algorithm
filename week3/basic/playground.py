# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        text1 = ''
        text2 = ''

        list1 = []
        list2 = []
        while l1 != None:
            list1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            list2.append(l2.val)
            l2 = l2.next

        l1 = list1
        l2 = list2

        

        while l1:
            text1 += str(l1.pop())

        while l2:
            text2 += str(l2.pop())

        result_rever_text = int(text1) + int(text2) # 정수
        result = str(result_rever_text)[::-1]

        return list(map(int, result))