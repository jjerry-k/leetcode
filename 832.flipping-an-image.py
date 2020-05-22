#
# @lc app=leetcode id=832 lang=python3
#
# [832] Flipping an Image
# Your runtime beats 9.8 % of python3 submissions
# Your memory usage beats 6 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [[1-A[i][::-1][j] for j in range(len(A[0]))] for i in range(len(A))]
# @lc code=end

