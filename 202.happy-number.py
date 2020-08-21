#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
# Your runtime beats 85.27 % of python3 submissions
# Your memory usage beats 50.65 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        tmp = sum([int(elem)**2 for elem in str(n)])
        return True if tmp == 1 else False if tmp == 4 else self.isHappy(tmp)
# @lc code=end