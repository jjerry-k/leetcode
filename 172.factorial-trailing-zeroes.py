#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
# Your runtime beats 5.04 % of python3 submissions.
# Your memory usage beats 10 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def trailingZeroes(self, n: int) -> int:
        return 0 if n < 5 else n//5 + self.trailingZeroes(n//5)
# @lc code=end
