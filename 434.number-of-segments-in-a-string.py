#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
# Your runtime beats 79.39 % of python3 submissions
# Your memory usage beats 69.43 % of python3 submissions (14.1 MB)
# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
# @lc code=end