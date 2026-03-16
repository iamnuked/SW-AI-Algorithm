# 해시 테이블 - 민균이의 비밀번호 (백준 브론즈1)
# 문제 링크: https://www.acmicpc.net/problem/9933


# 완

def reverse(pw :str):
    result = ""
    for rev_i in range(len(pw), 0, -1):
        result += pw[rev_i-1]
    return result

pw_dict = {}

rep = int(input())
for i in range(rep):
    key = input()
    pw_dict[key] = reverse(key)

for key in pw_dict.keys():
    if key in pw_dict.values():
        print(len(key), key[len(key)//2])
        break
