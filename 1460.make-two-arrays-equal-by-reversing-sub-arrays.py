#
# @lc app=leetcode id=1460 lang=python3
#
# [1460] Make Two Arrays Equal by Reversing Sub-arrays
# Your runtime beats 42.65 % of python3 submissions
# Your memory usage beats 63.17 % of python3 submissions (13.9 MB)
# @lc code=start
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)
# @lc code=end