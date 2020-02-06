#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0 : return 0
        tmp = haystack.split(needle)
        return -1 if len(tmp)==1 else len(tmp[0]) 
# @lc code=end

