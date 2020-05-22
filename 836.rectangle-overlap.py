#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
# Your runtime beats 98.31 % of python3 submissions
# Your memory usage beats 8.33 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return rec1[0] < rec2[2] and rec2[0] < rec1[2] and rec1[1] < rec2[3] and rec2[1] < rec1[3]
# @lc code=end

