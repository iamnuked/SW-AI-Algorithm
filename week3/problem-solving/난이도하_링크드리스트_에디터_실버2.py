# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406


class node:
    def __init__(self, ch):
        self.data = ch
        self.next = None
        self.prev = None

    
class linked_list:
    def __init__(self):
        self.head = None
        self.curser = None

    # 기존 문자 추가
    def opentxt(self, string):
        for ch in string:
            self.append(ch)
        return

    # L 왼쪽으로 이동 -> 문제 발생
    def left_shift(self):
        if self.curser.prev == None:
            return
        self.curser = self.curser.prev
        return


    # D 오른쪽으로 이동
    def right_shift(self):
        if self.curser.next == None:
            return
        self.curser = self.curser.next
        return


    # B 현재 노드 왼쪽 삭제 -> 한칸 왼쪽을 지우는 문제 발생
    def backspace(self):
        if self.curser == self.head:
            return
        elif self.curser.prev == self.head: # 맨 앞 글자 삭제인 경우 head 값 변경해줘야 함
            self.curser = self.curser.next
            self.curser.prev = None
            self.head = self.curser

        elif self.curser.next == None: # 끝 글자 삭제
            self.curser = self.curser.prev
            self.curser.next = None

        else: # 중간 글자 삭제인 경우
            self.curser.prev.next = self.curser.next
            self.curser.next.prev = self.curser.prev
            pass

    # P $ $라는 문자 커서 왼쪽에 추가
    def append(self, ch):

        new_node = node(ch)

        # 빈 상태
        if self.head == None:
            self.head = new_node
            self.curser = new_node

        # 끝 커서
        elif self.curser.next == None:
            new_node.prev = self.curser
            self.curser.next = new_node
            self.curser = self.curser.next

        # 앞 커서
        # elif self.curser.prev == None:
        #     pass
            
        else: # 중간 커서
            temp = self.curser.next # 커서 왼쪽 노드
            new_node.prev = self.curser
            self.curser.next = new_node

            temp.prev = new_node
            self.curser.next.next = temp # 기존 왼쪽 노드 합치기
            self.curser = self.curser.next



    # 출력
    def print_linked_list(self):
        velues = ""
        self.curser = self.head
        while self.curser != None:
            velues += self.curser.data
            self.curser = self.curser.next
        return velues


# 테스트 케이스
ll = linked_list()
ll.opentxt("abc")
ll.left_shift()
# ll.right_shift()

ll.backspace()
ll.append('1')
ll.append('2')
ll.append('3')
print(ll.print_linked_list())