#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
# Your runtime beats 17.48 % of python3 submissions
# Your memory usage beats 70.97 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        words = str.split(' ')
        return len(pattern) == len(words) and len(set(pattern)) == len(set(words)) == len(set(zip(words, pattern)))
# @lc code=end