  
#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
# Your runtime beats 11.14 % of python3 submissions
# Your memory usage beats 100 % of python3 submissions (12.9 MB)
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
# @lc code=end
