#
# @lc app=leetcode id=1725 lang=python3
#
# [1725] Number Of Rectangles That Can Form The Largest Square
# Your runtime beats 26.97 % of python3 submissions
# Your memory usage beats 48.34 % of python3 submissions (15 MB)
# @lc code=start
class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        max_length = max(min(i, j) for i, j in rectangles)
        return sum(min(i, j) == max_length for i, j in rectangles)
# @lc code=end