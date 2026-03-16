# 스택 - 스택 (백준 실버 4)
# 문제 링크: https://www.acmicpc.net/problem/10828

# 완


N = int(input())
stack = []

for _ in range(N):
    command = input()

    if command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        result = len(stack)
        if result == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        push_x = command.split(" ")
        stack.append(int(push_x[1]))



