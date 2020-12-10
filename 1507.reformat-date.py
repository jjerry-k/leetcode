#
# @lc app=leetcode id=1507 lang=python3
#
# [1507] Reformat Date
# Your runtime beats 40.53 % of python3 submissions
# Your memory usage beats 43.65 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def reformatDate(self, date: str) -> str:
        Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d, m, y = date.split(' ')
        result = f"{y}-{Month.index(m)+1:02}-{int(d[:-2]):02}"
        return result
# @lc code=end