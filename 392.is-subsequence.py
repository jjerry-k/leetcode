#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
# Your runtime beats 87.64 % of python3 submissions
# Your memory usage beats 10.62 % of python3 submissions (14.3 MB)
# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for elem in s:
            if elem not in t : return False
            elem_index = t.index(elem)
            t =  t[elem_index+1:]
        return True
# @lc code=end