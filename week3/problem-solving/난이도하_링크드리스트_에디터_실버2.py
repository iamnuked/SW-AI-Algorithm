# 링크드리스트 - 에디터 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/1406

# 더미 헤드 하나 추가해야됨

# 시간초과

class node:
    def __init__(self, ch=""):
        self.data = ch
        self.next = None
        self.prev = None

    
class linked_list:
    def __init__(self):
        self.dummy_head = node()
        self.curser = self.dummy_head
        

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


    # B 현재 노드 삭제
    def backspace(self):
        # 맨 앞인 경우
        if self.curser == self.dummy_head:
            return
        # 끝인 경우
        elif self.curser.next == None:
            self.curser = self.curser.prev
            self.curser.next = None
            return
        # 중간인 경우
        else:
            self.curser.prev.next = self.curser.next
            self.curser.next.prev = self.curser.prev
            self.curser = self.curser.prev


    # P $ $라는 문자 커서 왼쪽에 추가
    def append(self, ch):

        new_node = node(ch)

        # 빈 상태
        if self.dummy_head.next == None:
            self.dummy_head.next = new_node
            new_node.prev = self.dummy_head
            self.curser = new_node

        # 끝 커서
        elif self.curser.next == None:
            new_node.prev = self.curser
            self.curser.next = new_node
            self.curser = new_node

        else: # 중간 커서
            temp = self.curser.next # 커서 왼쪽 노드
            new_node.prev = self.curser
            new_node.next = temp
            self.curser.next = new_node
            temp.prev = new_node
            self.curser = new_node



    # 출력
    def print_linked_list(self):
        velues = []
        temp = self.curser
        self.curser = self.dummy_head

        while self.curser != None:
            velues.append(self.curser.data)
            self.curser = self.curser.next


        self.curser = temp
        return print(''.join(velues))




# 입력 값 관련
ll = linked_list()

file = input()
ll.opentxt(file)

M = int(input())

for i in range(M):
    command = input().split()
    if command[0] == 'L': # 왼쪽으로 이동
        ll.left_shift()
    elif command[0] == 'D':
        ll.right_shift()
    elif command[0] == 'B':
        ll.backspace()
    elif command[0] == 'P':
        ll.append(command[1])


ll.print_linked_list()