#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
# Your runtime beats 98.99 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.8 MB)

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = abs(dividend) // abs(divisor)
        quotient = quotient if dividend*divisor >0 else -quotient
        return min(max(-2147483648, quotient), 2147483647)
# @lc code=end

