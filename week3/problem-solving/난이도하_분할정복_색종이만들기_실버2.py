# 분할정복 - 색종이 만들기 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/2630



# test case

N = 8
matrix =   [[1, 1, 0, 0 ,0, 0, 1, 1],
            [1, 1, 0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 1, 1, 1, 1, 1, 1]]
count = 0

# 재귀로 가보자
def cut(start_xy, end_xy):
    global count
    x_mid = (start_xy[0]+end_xy[0])//2
    y_mid = (start_xy[1]+end_xy[1])//2

    print(start_xy, end_xy, x_mid, y_mid)

    # 종이 길이가 1인 경우
    if end_xy[0] - start_xy[0] == 1:
        count += 1
        return
    # 모든 숫자 같을 경우
    part = matrix[start_xy[0]:end_xy[0]+1][start_xy[1]:end_xy[1]+1]
    if all(x == part[0][0] for x in part):
        count += 1
        return
    cut([start_xy[0], start_xy[1]],
        [x_mid, y_mid] ) # 좌상
    cut([x_mid, start_xy[1]],
        [end_xy[0]+1, y_mid]) # 우상
    cut([start_xy[0], y_mid],
        [x_mid+1, end_xy[1]]) # 좌하
    cut([x_mid+1, y_mid],
        [end_xy[0]+1, end_xy[1]]) # 우하

    pass


cut([0, 0], [7, 7])

print(count)