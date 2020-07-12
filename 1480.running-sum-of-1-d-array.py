#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
# Your runtime beats 27.25 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        return [sum(nums[:i+1]) for i in range(len(nums))]
# @lc code=end