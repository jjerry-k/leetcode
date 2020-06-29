#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
# Your runtime beats 98.96 % of python3 submissions
# Your memory usage beats 8.7 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num in (1, 4): return True
        elif num % 4 or num < 1: return False
        return self.isPowerOfFour(num // 4)
# @lc code=end

