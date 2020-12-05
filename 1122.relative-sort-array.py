#
# @lc app=leetcode id=1122 lang=python3
#
# [1122] Relative Sort Array
# Your runtime beats 90.5 % of python3 submissions
# Your memory usage beats 8.53 % of python3 submissions (14.4 MB)
# @lc code=start
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        index = {v:i for i, v in enumerate(arr2)}
        return sorted(arr1, key=lambda x: index.get(x, x+1000))
# @lc code=end