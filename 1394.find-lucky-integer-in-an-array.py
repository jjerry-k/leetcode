#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
# Your runtime beats 71.17 % of python3 submissions
# Your memory usage beats 80.12 % of python3 submissions (13.8 MB)
# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for i in sorted(list(set(arr[::-1])), reverse=True):
            if arr.count(i) == i: return i
        return -1
# @lc code=end