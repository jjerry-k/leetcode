#
# @lc app=leetcode id=1422 lang=python3
#
# [1422] Maximum Score After Splitting a String
# Your runtime beats 29.46 % of python3 submissions
# Your memory usage beats 96.05 % of python3 submissions (13.6 MB)
# @lc code=start
class Solution:
    def maxScore(self, s: str) -> int:
        max_val = 0
        for i in range(1, len(s)):
            tmp_val = s[:i].count("0") + s[i:].count("1")
            max_val = tmp_val if tmp_val > max_val else max_val
        return max_val
# @lc code=end

