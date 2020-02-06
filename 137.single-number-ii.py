#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in sorted(set(nums)):
            if nums.count(i) == 1:
                return i
# @lc code=end

