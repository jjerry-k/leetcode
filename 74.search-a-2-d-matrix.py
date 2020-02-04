#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
# Your runtime beats 94 % of python3 submissions
# Your memory usage beats 5.88 % of python3 submissions (14.9 MB)
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return bool(sum([target in i for i in matrix]))
# @lc code=end

