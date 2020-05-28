#
# @lc app=leetcode id=1351 lang=python3
#
# [1351] Count Negative Numbers in a Sorted Matrix
# Your runtime beats 40.57 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (14.6 MB)
# @lc code=start
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([1 for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j]<0])
# @lc code=end

