"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in nums:
            for j in nums:
                if i+j == target and nums.index(i) != nums.index(j):
                    List = [nums.index(i), nums.index(j)]
                    print(List)
                    return List


a = Solution()
a.twoSum([2,7,11,15], 9)


b =[1,2,3]
# Time Limit Exceeded
# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         new_dict = {n:i for n, i in enumerate(nums)}
#         for key in new_dict:
#             for k in new_dict:
#                 if new_dict[key] + new_dict[k] == target and new_dict[key] != new_dict[k]:
#                     print([key, k])
#                     return [key, k]
#         print(new_dict)
#
#
#
#
# a = Solution()
# a.twoSum([2,7,11,15], 9)