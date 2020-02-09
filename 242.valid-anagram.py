#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
# Your runtime beats 16.69 % of python3 submissions
# Your memory usage beats 34.38 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
# @lc code=end