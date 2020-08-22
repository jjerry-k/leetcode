#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
# Your runtime beats 20.1 % of python3 submissions
# Your memory usage beats 5.26 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num == int(num ** 0.5)**2
# @lc code=end