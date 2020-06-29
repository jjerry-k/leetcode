#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
# Your runtime beats 51.97 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=start
class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        else:
            return self.addDigits(sum([int(i) for i in str(num)]))
# @lc code=end