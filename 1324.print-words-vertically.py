#
# @lc app=leetcode id=1324 lang=python3
#
# [1324] Print Words Vertically
# Your runtime beats 100 % of python3 submissions
# Your memory usage beats 86.79 % of python3 submissions (14.2 MB)
# @lc code=start
class Solution:
    def printVertically(self, s: str) -> List[str]:
        from itertools import zip_longest
        return [''.join(zips).rstrip() for zips in zip_longest(*s.split(), fillvalue=' ')]
# @lc code=end