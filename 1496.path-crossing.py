#
# @lc app=leetcode id=1496 lang=python3
#
# [1496] Path Crossing
# Your runtime beats 86.27 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        curr = (0, 0)
        coordinates = {curr}
        direction = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for p in path:
            curr = (curr[0] + direction[p][0], curr[1] + direction[p][1]) 
            if curr in coordinates: return True
            coordinates.add(curr)
        return False
# @lc code=end