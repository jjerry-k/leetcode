#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
# Your runtime beats 99.39 % of python3 submissions
# Your memory usage beats 34.41 % of python3 submissions (14 MB)
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        string = "abcdefghijklmnopqrstuvwxyz"
        elem_index = [s.index(al) for al in string if s.count(al) == 1]
        return sorted(elem_index)[0] if elem_index else -1
# @lc code=end