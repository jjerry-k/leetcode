#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
# Your runtime beats 27.62 % of python3 submissions
# Your memory usage beats 78 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        cc = int(c ** 0.5)
        left = 0
        right = cc
        while left <= right:
            res = left ** 2 + right ** 2
            if res == c:
                return True
            elif res < c:
                left += 1
            elif res > c:
                right -= 1
        return False
# @lc code=end

