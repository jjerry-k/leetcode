#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
# Your runtime beats 5.48 % of python3 submissions
# Your memory usage beats 53.33 % of python3 submissions (14.6 MB)
# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in sorted(set(nums)):
            if nums.count(i) == 1:
                return i
# @lc code=end

