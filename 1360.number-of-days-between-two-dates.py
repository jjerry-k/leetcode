#
# @lc app=leetcode id=1360 lang=python3
#
# [1360] Number of Days Between Two Dates
# Your runtime beats 46.9 % of python3 submissions
# Your memory usage beats 69.14 % of python3 submissions (13.8 MB)
# @lc code=start
from datetime import datetime
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        return abs((datetime.strptime(date2, '%Y-%m-%d').date() - datetime.strptime(date1, '%Y-%m-%d').date()).days)
# @lc code=end