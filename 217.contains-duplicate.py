#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
# Your runtime beats 45.53 % of python3 submissions
# Your memory usage beats 62.1 % of python3 submissions (19.2 MB)
# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(list(set(nums)))
# @lc code=end

