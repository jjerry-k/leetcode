#
# @lc app=leetcode id=1260 lang=python3
#
# [1260] Shift 2D Grid
# Your runtime beats 91.15 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=start
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k = k%(m*n)
        flatten = [grid[i][j] for i in range(m) for j in range(n)]
        flatten = flatten[-k:]+flatten[:-k]
        output = [flatten[i:i+n] for i in range(0, m*n, n)]
        return output
# @lc code=end