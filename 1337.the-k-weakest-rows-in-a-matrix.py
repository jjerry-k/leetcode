#
# @lc app=leetcode id=1337 lang=python3
#
# [1337] The K Weakest Rows in a Matrix
# Your runtime beats 48.95 % of python3 submissions
# Your memory usage beats 11.87 % of python3 submissions (14.7 MB)
# @lc code=start
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = {row_idx:sum(mat[row_idx]) for row_idx in range(len(mat))}
        return sorted(soldiers, key=lambda x: soldiers[x])[:k]
# @lc code=end