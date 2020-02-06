#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
# Your runtime beats 44.63 % of python3 submissions
# Your memory usage beats 98.51 % of python3 submissions (13.5 MB)
# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return sum([1 for i in nums if i < target])

# @lc code=end

