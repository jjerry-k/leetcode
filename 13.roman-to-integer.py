#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
# Your runtime beats 95.64 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        sym2val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        integer = 0
        prev_roman = 'I'
        for cur_roman in s[::-1]:
            if sym2val[prev_roman] <= sym2val[cur_roman]:  integer += sym2val[cur_roman]
            else : integer -= sym2val[cur_roman]
            prev_roman = cur_roman
        return integer
# @lc code=end