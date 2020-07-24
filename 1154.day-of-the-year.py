#
# @lc app=leetcode id=1154 lang=python3
#
# [1154] Day of the Year
# Your runtime beats 67.93 % of python3 submissions
# Your memory usage beats 33.33 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def dayOfYear(self, date: str) -> int:
        y, m, d = [int(i) for i in date.split('-')]
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if (y % 400) == 0 or ((y % 4 == 0) and (y % 100 != 0)): days[1] = 29
        return d + sum(days[:m-1])
# @lc code=end