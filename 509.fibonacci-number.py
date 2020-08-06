#
# @lc app=leetcode id=509 lang=python3
#
# [509] Fibonacci Number
<<<<<<< HEAD
# Your runtime beats 8.23 % of python3 submissions
# Your memory usage beats 36.23 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        return self.fib(N-1) + self.fib(N-2) if N > 1 else N
=======
# Your runtime beats 11.46 % of python3 submissions
# Your memory usage beats 11.54 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def fib(self, N: int) -> int:
        return N if N<2 else self.fib(N-1) + self.fib(N-2) 
>>>>>>> 4e6f946f5bc34fe3acebb68901590bf53845aa34
# @lc code=end