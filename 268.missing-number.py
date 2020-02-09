#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
# Your runtime beats 71.44 % of python3 submissions
# Your memory usage beats 56.45 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)
# @lc code=end