# def removeDuplicates(nums):

#     temp = 0
#     for i in range(len(nums)):
#         if len(nums) == i:
#             break

#         temp = nums[i]
#         if temp == nums[i+1]:
#             nums.remove(i)
#         else:
#             temp = nums[i]

#     return len(nums), nums

nums = [0,0,1,1,1,2,2,3,3,4]



class Solution(object):
    def removeDuplicates(self, nums):
        temp = 0
        for i in range(len(nums)):
            if len(nums) == i+1:
                break

            temp = nums[i]
            if nums[i+1] == temp:
                nums.pop(i)
            else:
                temp = nums[i+1]

        return len(nums), nums


print(Solution.removeDuplicates("" , nums))


