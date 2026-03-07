# 문자열 - IPv6 (백준 실버1)
# 문제 링크: https://www.acmicpc.net/problem/3107


addr = input()


addr1_list = addr.split(":")
addr2_list = addr.split("::")

result = ""


def add_zeros(addr1_list):
    result = ""
    for x in addr1_list:
        rev = x[::-1]
        for _ in range(4-len(rev)):
            rev = rev + '0'
        forward_addr = rev[::-1]
        result = result + forward_addr + ':'

    return result[:-1]

def make_block(addr2_list, addr1_list):
    string = ":"
    count = 11 - len(addr2_list) - len(addr1_list)
    for _ in range(count):
        string = string + "0000:"
    return string

result = ""

if len(addr2_list) == 2:
    result = add_zeros(addr2_list[0].split(':')) + make_block(addr2_list, addr1_list) + add_zeros(addr2_list[1].split(':'))

elif addr[0] == ':' and addr[1] == ':':
    result = make_block(addr2_list, addr1_list) + add_zeros(addr2_list[0].split(':'))

elif addr[-1] == ':' and addr[-2] == ':':
    result = add_zeros(addr2_list[0].split(':')) + make_block(addr2_list, addr1_list)
else:
    result = add_zeros(addr1_list)


print(result)