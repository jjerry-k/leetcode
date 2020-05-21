#
# @lc app=leetcode id=867 lang=python3
#
# [867] Transpose Matrix
# Your runtime beats 11.63 % of python3 submissions
# Your memory usage beats 5.72 % of python3 submissions (14.6 MB)
# @lc code=start
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[A[row][col] for row in range(len(A))] for col in range(len(A[0]))]
# @lc code=end

