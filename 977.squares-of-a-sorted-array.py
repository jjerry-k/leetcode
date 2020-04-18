#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
# Your runtime beats 88.07 % of python3 submissions
# Your memory usage beats 5.95 % of python3 submissions (15.8 MB)
# @lc code=start
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i**2 for i in A])
# @lc code=end

