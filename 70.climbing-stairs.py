#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
# Your runtime beats 91.35 % of python3 submissions
# Your memory usage beats 5.97 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return n
        prev, curr = 1, 2
        for i in range(2, n):
            tmp = curr
            curr = prev + curr
            prev = tmp
        return curr
# @lc code=end