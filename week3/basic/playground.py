class Solution:
    def simplifyPath(self, path: str) -> str:
        raw_path = path.split('/')
        new_path = []
        for x in raw_path:
            if x == '':
                continue
            if x == '.':
                continue
            if x == '..' or x == '.. ':
                if len(new_path) > 0:
                    new_path.pop()
            else:
                new_path.append(x)

        result = '/' + '/'.join(new_path)

        return result
    