#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
# Your runtime beats 5.35 % of python3 submissions
# Your memory usage beats 21.31 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in sorted(set(nums)):
            if nums.count(i) == 1:
                return i
# @lc code=end

