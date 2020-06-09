#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
# Your runtime beats 7.01 % of python3 submissions
# Your memory usage beats 59.81 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MIN, INT_MAX = -2**31, 2**31-1

        s = list(str.strip(' '))

        if len(s) == 0: return 0
        
        sign = -1 if s[0] == "-" else 1
        if s[0] in ["+", "-"]: s=s[1:]

        digit, i = 0, 0
        while i < len(s) and s[i].isdigit() :
            digit = digit*10 + ord(s[i]) - ord('0')
            i += 1
        return max(INT_MIN, min(sign * digit, INT_MAX))
# @lc code=end