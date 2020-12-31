#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
# Your runtime beats 50.19 % of python3 submissions
# Your memory usage beats 57.55 % of python3 submissions (21.1 MB)
# @lc code=start
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1 for _ in range(len(nums))]
        left_side = 1
        right_side = 1
        for i in range(len(nums)):
            result[i] *= left_side
            result[-1-i] *= right_side
            left_side *= nums[i]
            right_side *= nums[-1-i]
        return result
# @lc code=end