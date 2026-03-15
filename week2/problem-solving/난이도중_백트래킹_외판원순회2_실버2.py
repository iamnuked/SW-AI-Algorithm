# 백트래킹 - 외판원 순회 2 (백준 실버2)
# 문제 링크: https://www.acmicpc.net/problem/10971

'''
시작지점은 고정

-> 조합 문제
경로가 같으면 어느 도시에서 시작하든 거리는 같음




'''
# city_count = input()
# city_matrix = input()

city_count = "4"
city_matrix1 = "0 10 15 20"
city_matrix2 = "5 0 9 10" 
city_matrix3 = "6 13 0 12"
city_matrix4 = "8 8 9 0"

city_matrix = []
city_matrix1 = city_matrix1.split(" ")
city_matrix2 = city_matrix2.split(" ")
city_matrix3 = city_matrix3.split(" ")
city_matrix4 = city_matrix4.split(" ")

city_matrix.append(city_matrix1)
city_matrix.append(city_matrix2)
city_matrix.append(city_matrix3)
city_matrix.append(city_matrix4)

print(city_matrix)



def tsp():
    result = []

    def back(start, curr_arr):
        if len(curr_arr) == 4:
            result.append(curr_arr.copy)
            return
        

        for i in range(start, 5):
            if city_matrix[start][i] == 0:
                return
            curr_arr.append(i)
            back(i+1, curr_arr)
            curr_arr.pop()

        return
    

    back(0, [])
    print(result)
    return

tsp()