class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        char_list = [[], [], ["abc"], ["def"], ["ghi"], ["jkl"], ["mno"], ["pqrs"], ["tuv"], ["wxyz"]]
        nums = list(map(int, digits)) # nums = [2, 3]


        def comb(idx, curr):
            num = nums[idx] # 선택
            string = char_list[num]
            if len(curr) == len(nums): # 베이스 케이스
                return result.append(curr)

            for ch in string:
                curr.append():



            
        


        comb(0, [])
        return print(result)



Solution.letterCombinations("", "23")