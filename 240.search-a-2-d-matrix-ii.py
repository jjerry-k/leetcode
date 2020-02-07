#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
# Your runtime beats 21.8 % of python3 submissions
# Your memory usage beats 96.3 % of python3 submissions (17.3 MB)
# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        r = len(matrix)
        if r==0: return False
        c = len(matrix[0])
        flatten = [matrix[i][j] for i in range(r) for j in range(c)]
        return target in flatten
# @lc code=end