#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
# Your runtime beats 68.02 % of python3 submissions
# Your memory usage beats 5.26 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
# @lc code=end

