#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
# Your runtime beats 95.45 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.7 MB)
# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return str(bin(int(a, 2) + int(b, 2)))[2:]
# @lc code=end

