#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
# Your runtime beats 39.02 % of python3 submissions
# Your memory usage beats 57.05 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for i in range(len(num1)):
            n1 = n1*10 + ord(num1[i])-48
        for i in range(len(num2)):
            n2 = n2*10 + ord(num2[i])-48
        return str(n1+n2)
# @lc code=end