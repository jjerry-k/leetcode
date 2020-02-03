#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # num_set=list(range(min(nums), max(nums)+1))
        # return num_set[[nums.count(i) for i in range(min(nums), max(nums)+1)].index(1)]
        for i in sorted(set(nums)):
            if nums.count(i) == 1:
                return i
# @lc code=end

