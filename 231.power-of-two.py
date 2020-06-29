#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
# Your runtime beats 49.43 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)
# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and (n&(n-1))==0
# @lc code=end

