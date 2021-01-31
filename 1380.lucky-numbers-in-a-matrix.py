#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
# Your runtime beats 48.5 % of python3 submissions
# Your memory usage beats 13.98 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = [min(row) for row in matrix]
        col_max = [max(col) for col in zip(*matrix)]
        return [cell for i, row in enumerate(matrix) for j, cell in enumerate(row) if row_min[i] == col_max[j]]
# @lc code=end