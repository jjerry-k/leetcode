#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
# Your runtime beats 21.15 % of python3 submissions
# Your memory usage beats 34.4 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == int(num ** 0.5)**2
# @lc code=end