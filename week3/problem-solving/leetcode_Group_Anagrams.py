# https://leetcode.com/problems/group-anagrams/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs = sorted(strs)
        sorted_str = []

        for str in strs:
            sorted_str.append(''.join(sorted(str)))

        outer_list = []

        # 딕셔너리 안에 그룹화
        str_dict = {}
        for idx, str in enumerate(sorted_str):
            str_dict.setdefault(str, []).append(strs[idx])

        # 딕셔너리를 리스트로 파싱해서 길이 순으로 정렬
        result = list(str_dict.values())
        result.sort(key= len)
        return result

        