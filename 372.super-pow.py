#
# @lc app=leetcode id=372 lang=python3
#
# [372] Super Pow
# Your runtime beats 83.11 % of python3 submissions
# Your memory usage beats 25 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        return pow(a, int("".join(map(str, b))), 1337)
# @lc code=end