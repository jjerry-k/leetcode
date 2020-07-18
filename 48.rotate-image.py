#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
# Your runtime beats 21.94 % of python3 submissions
# Your memory usage beats 95.8 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix[0]))]
# @lc code=end

