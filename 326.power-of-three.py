#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
# Your runtime beats 82.61 % of python3 submissions
# Your memory usage beats 7.41 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n in (1, 3): return True
        elif n % 3 or n < 1: return False
        return self.isPowerOfThree(n // 3)
# @lc code=end
