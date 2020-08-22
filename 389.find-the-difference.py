#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
# Your runtime beats 84.16 % of python3 submissions
# Your memory usage beats 30.89 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s, t = sorted(s), sorted(t)
        return t[-1] if s == t[:-1] else [x[1] for x in zip(s, t) if x[0] != x[1]][0]
# @lc code=end