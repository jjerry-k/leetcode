#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
# Your runtime beats 37.42 % of python3 submissions
# Your memory usage beats 10 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1 << len(format(num, 'b'))
        return mask - 1 - num
# @lc code=end

