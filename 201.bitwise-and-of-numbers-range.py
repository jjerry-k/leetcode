#
# @lc app=leetcode id=201 lang=python3
#
# [201] Bitwise AND of Numbers Range
# Your runtime beats 93.46 % of python3 submissions
# Your memory usage beats 57.2 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        i = 0
        while m != n:
            m >>= 1
            n >>= 1
            i += 1
        return n << i
# @lc code=end