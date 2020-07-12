#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
# Your runtime beats 69.17 % of python3 submissions
# Your memory usage beats 74.19 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums)==0 or min(nums) > 1 or max(nums) < 1: return 1
        for i in range(max(0, min(nums)), max(0, max(nums)+2)):
            if i > 0 and i not in nums: return i
# @lc code=end

