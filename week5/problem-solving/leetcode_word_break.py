# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150

# class Solution:
#     def wordBreak(self, s: str, wordDict: List[str]) -> bool:
#         count = len(wordDict)
#         for word in wordDict:
#             s = s.replace(word, "-")

#         if count <= s.count("-"):
#             return True
#         else:
#             return False
        
# s = "cars"
# wordDict = ["car","ca","rs"]



# count = len(wordDict)
# for word in wordDict:
#     s = s.replace(word, "")
#     print(s)

# if s == "":
#     print(True)
# else:
#     print(False)



class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False]* (n+1)
        dp[0] = True

        for i in range(1, n+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break

        return dp[n]
