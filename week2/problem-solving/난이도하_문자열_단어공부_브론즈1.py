# 문자열 - 단어 공부 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/1157

# 시간 초과
# string = input()
# list = [1]*len(string)
# string = string.upper()
# for x in range(len(string)):
#     for y in range(x):
#         if string[y] == string[x]:
#             list[y] = list[y] + 1


            
# max_value = max(list)
# index = list.index(max_value)
# count = 0
# for x in list:
#     if max_value == x:
#         count = count + 1

# if count > 1:
#     print("?")
# else:
#     print(string[index])


# string = ""
# string = input()
# list = [0]*len(string)

# for i in range(string):
#     for j in range(string):
#         if string[i] == string[j]:
#             string.pop(1)



string = input()
string = string.upper()
ch_list = []

for i in string:
    ch_list.append(i)

ch = set()
for i in string:
    ch.add(i)

ch = list(ch)



ch_count = []
for i in ch:
    ch_count.append(ch_list.count(i))

max_count = max(ch_count)


idx = [i for i, v in enumerate(ch_count) if v == max_count]


if len(idx) > 1:
    print("?")
else:
    print(ch[idx[0]])


