#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
# Your runtime beats 46.71 % of python3 submissions
# Your memory usage beats 15 % of python3 submissions (14.5 MB)
# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]

# @lc code=end