# https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150
# 스택, 디렉토리 주소

class Solution:
    def simplifyPath(self, path: str) -> str:
        raw_path = path.split('/')
        new_path = []
        for x in raw_path:
            if x == '' or x == '.':
                continue
            elif x == '..' or x == '.. ':
                if new_path:
                    new_path.pop()
            else:
                new_path.append(x)

        result = '/' + '/'.join(new_path)

        return result
    