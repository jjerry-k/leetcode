#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
# Your runtime beats 86.95 % of python3 submissions
# Your memory usage beats 96.15 % of python3 submissions (13.2 MB)
# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([i[::-1] for i in s.split(' ')])
# @lc code=end

