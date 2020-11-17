#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
# Your runtime beats 11.95 % of python3 submissions
# Your memory usage beats 6.79 % of python3 submissions (19.3 MB)
# @lc code=start
import itertools

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return max([(i-1)*(j-1) for i, j in itertools.combinations(nums, 2)])
# @lc code=end