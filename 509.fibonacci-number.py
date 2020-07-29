#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
# Your runtime beats 11.46 % of python3 submissions
# Your memory usage beats 11.54 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        return N if N<2 else self.fib(N-1) + self.fib(N-2) 
# @lc code=end