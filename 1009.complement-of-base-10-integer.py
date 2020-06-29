#
# @lc app=leetcode id=1009 lang=python3
#
# [1009] Complement of Base 10 Integer
# Your runtime beats 36.92 % of python3 submissions
# Your memory usage beats 6.67 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        mask = 1 << len(format(N, 'b'))
        return mask - 1 - N
# @lc code=end