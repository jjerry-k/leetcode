#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        a = int(dividend/divisor)
        return  a if a<2**31 else a-1
# @lc code=end

