#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
# Your runtime beats 92.14 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.6 MB)
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n)[2:].count('1')
# @lc code=end