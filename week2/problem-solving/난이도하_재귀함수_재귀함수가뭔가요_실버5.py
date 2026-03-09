# 재귀함수 - 재귀함수가 뭔가요? (백준 실버5)
# 문제 링크: https://www.acmicpc.net/problem/17478

'''
1. 재귀함수 왓? 출력
2. n = 0 -> 함수라네 출력 2-1. n = n-1
    else -> 이야기보따리 출력

3. 회수작업 -> 라고 답변하였지 출력

직선 * n 만큼 str 앞에 추가
'''

str1 = "\"재귀함수가 뭔가요?\""

str2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n"
str3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n"
str4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""


str5 = "\"재귀함수는 자기 자신을 호출하는 함수라네\""

str6 = "라고 답변하였지."

line = "____"
count = 0




def jh_says(n :int, count):
    zigseon = ""
    for i in range(count):
        zigseon = zigseon + line

    print(zigseon+str1)
    if n == 0:
        print(zigseon+str5)
        print(zigseon+str6)
        return
    
    print(zigseon+str2 + zigseon+str3 + zigseon+str4)
    count = count + 1
    return jh_says(n-1,count), print(zigseon + str6)


n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
jh_says(n ,0)

