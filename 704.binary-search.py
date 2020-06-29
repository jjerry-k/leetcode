#
# @lc app=leetcode id=704 lang=python3
#
# [704] Binary Search
# Your runtime beats 73.15 % of python3 submissions
# Your memory usage beats 6.45 % of python3 submissions (14.9 MB)
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return nums.index(target) if target in nums else -1
# @lc code=end

