#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
# Your runtime beats 99.72 % of python3 submissions
# Your memory usage beats 32.85 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
# @lc code=end

