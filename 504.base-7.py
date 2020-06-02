#
# @lc app=leetcode id=504 lang=python3
#
# [504] Base 7
# Your runtime beats 99.63 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (13.7 MB)
# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        if num < 0: return '-' + self.convertToBase7(-num)
        elif num < 7: return str(num)
        return self.convertToBase7(num//7) + str(num%7)
# @lc code=end