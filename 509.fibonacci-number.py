#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
# Your runtime beats 8.23 % of python3 submissions
# Your memory usage beats 36.23 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        return self.fib(N-1) + self.fib(N-2) if N > 1 else N
# @lc code=end