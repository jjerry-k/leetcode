#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
# Your runtime beats 63.46 % of python3 submissions
# Your memory usage beats 12.81 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        rect1 = (C-A) * (D-B)
        rect2 = (G-E) * (H-F)
        intersection = max(0, min(C, G) - max(A, E)) * max(0, min(D, H) - max(B, F))

        return (rect1 + rect2) - intersection
# @lc code=end